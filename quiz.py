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