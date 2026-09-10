from quiz import Question, Quiz


# Tests for the Question class.

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


# Tests for the Quiz class.

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


def test_calculate_category_performance():
    """Test that category performance is calculated correctly."""
    questions = [
        Question(
            question_text="Population question",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            category="Population",
            source="Test source"
        ),
        Question(
            question_text="Population question 2",
            options=["A", "B", "C", "D"],
            correct_answer="B",
            category="Population",
            source="Test source"
        ),
        Question(
            question_text="Economic question",
            options=["A", "B", "C", "D"],
            correct_answer="C",
            category="Economic",
            source="Test source"
        )
    ]

    quiz = Quiz(questions)

    quiz.submit_answer(questions[0], "A")
    quiz.submit_answer(questions[1], "A")
    quiz.submit_answer(questions[2], "C")

    performance = quiz.calculate_category_performance()

    assert performance["Population"]["correct"] == 1
    assert performance["Population"]["total"] == 2
    assert performance["Population"]["percentage"] == 50.0

    assert performance["Economic"]["correct"] == 1
    assert performance["Economic"]["total"] == 1
    assert performance["Economic"]["percentage"] == 100.0


def test_perfect_quiz_score():
    """Test that a quiz with every answer correct scores 100%."""
    questions = [
        Question(
            question_text="Question 1",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            category="Test",
            source="Test source"
        ),
        Question(
            question_text="Question 2",
            options=["A", "B", "C", "D"],
            correct_answer="B",
            category="Test",
            source="Test source"
        ),
        Question(
            question_text="Question 3",
            options=["A", "B", "C", "D"],
            correct_answer="C",
            category="Test",
            source="Test source"
        )
    ]

    quiz = Quiz(questions)

    quiz.submit_answer(questions[0], "A")
    quiz.submit_answer(questions[1], "B")
    quiz.submit_answer(questions[2], "C")

    assert quiz.score == 3
    assert quiz.calculate_percentage() == 100.0


def test_zero_score_quiz():
    """Test that a quiz with every answer incorrect scores 0%."""
    questions = [
        Question(
            question_text="Question 1",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            category="Test",
            source="Test source"
        ),
        Question(
            question_text="Question 2",
            options=["A", "B", "C", "D"],
            correct_answer="B",
            category="Test",
            source="Test source"
        ),
        Question(
            question_text="Question 3",
            options=["A", "B", "C", "D"],
            correct_answer="C",
            category="Test",
            source="Test source"
        )
    ]

    quiz = Quiz(questions)

    quiz.submit_answer(questions[0], "B")
    quiz.submit_answer(questions[1], "C")
    quiz.submit_answer(questions[2], "D")

    assert quiz.score == 0
    assert quiz.calculate_percentage() == 0.0