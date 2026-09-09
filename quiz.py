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
        """Initialise a quiz with a list of questions and a score of zero."""
        self.questions = questions
        self.score = 0

    def submit_answer(self, question: Question, answer: str) -> None:
        """Submit an answer and increase the score when it is correct."""
        # Use the Question object's method to check whether the answer is correct.
        if question.is_correct(answer):
            self.score += 1

    def calculate_percentage(self) -> float:
        """Calculate and return the quiz score as a percentage."""
        # Prevent a division-by-zero error if a quiz contains no questions.
        if not self.questions:
            return 0.0

        # Convert the raw score into a percentage of the available marks.
        return (self.score / len(self.questions)) * 100