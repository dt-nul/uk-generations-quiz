from quiz import Question, Quiz


def test_correct_answer_returns_true():
    """Test that Question returns True when the correct answer is supplied."""
    question = Question(
        question_text="Which generation had the largest UK population in 2024?",
        options=["Gen Z", "Millennials", "Gen X", "Baby Boomers"],
        correct_answer="Millennials",
        category="Population",
        source="Statista / ONS"
    )

    assert question.is_correct("Millennials") is True


def test_incorrect_answer_returns_false():
    """Test that Question returns False when an incorrect answer is supplied."""
    question = Question(
        question_text="Which generation had the largest UK population in 2024?",
        options=["Gen Z", "Millennials", "Gen X", "Baby Boomers"],
        correct_answer="Millennials",
        category="Population",
        source="Statista / ONS"
    )

    assert question.is_correct("Gen Z") is False


def test_quiz_starts_with_zero_score():
    """Test that a new quiz starts with a score of zero."""
    quiz = Quiz([])

    assert quiz.score == 0

def test_correct_answer_increases_score():
    """Test that submitting a correct answer increases the quiz score."""
    question = Question(
        question_text="Which generation had the largest UK population in 2024?",
        options=["Gen Z", "Millennials", "Gen X", "Baby Boomers"],
        correct_answer="Millennials",
        category="Population",
        source="Statista / ONS"
    )

    quiz = Quiz([question])
    quiz.submit_answer(question, "Millennials")

    assert quiz.score == 1

def test_calculate_percentage():
    """Test that the quiz calculates the correct percentage score."""
    question = Question(
        question_text="Test question",
        options=["A", "B", "C", "D"],
        correct_answer="A",
        category="Test",
        source="Test source"
    )

    quiz = Quiz([question])
    quiz.submit_answer(question, "A")

    assert quiz.calculate_percentage() == 100.0


def test_empty_quiz_percentage_is_zero():
    """Test that an empty quiz returns zero rather than causing an error."""
    quiz = Quiz([])

    assert quiz.calculate_percentage() == 0.0