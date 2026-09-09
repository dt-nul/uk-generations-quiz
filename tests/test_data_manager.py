import pandas as pd
from data_manager import save_result


def test_save_result_creates_file(tmp_path):
    """Test that a quiz result is saved to a CSV file."""
    results_file = tmp_path / "results.csv"

    save_result(
        name="Test User",
        score=7,
        total_questions=10,
        percentage=70.0,
        result="Pass",
        file_path=str(results_file)
    )

    assert results_file.exists()

def test_save_result_writes_result_data(tmp_path):
    """Test that the saved CSV contains the expected result data."""
    results_file = tmp_path / "results.csv"

    save_result(
        name="Test User",
        score=7,
        total_questions=10,
        percentage=70.0,
        result="Pass",
        file_path=str(results_file)
    )

    data = pd.read_csv(results_file)

    assert list(data.columns) == [
        "name",
        "date_time",
        "score",
        "total_questions",
        "percentage",
        "result"
    ]
    assert data.loc[0, "name"] == "Test User"
    assert data.loc[0, "score"] == 7
    assert data.loc[0, "percentage"] == 70.0
    assert data.loc[0, "result"] == "Pass"