import pandas as pd
from data_manager import load_results, save_result


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

def test_load_results_returns_dataframe(tmp_path):
    """Test that saved results can be loaded into a pandas DataFrame."""
    results_file = tmp_path / "results.csv"

    results_file.write_text(
        "name,date_time,score,total_questions,percentage,result\n"
        "Test User,2026-09-09 20:00:00,7,10,70.0,Pass\n"
    )

    data = load_results(str(results_file))

    assert isinstance(data, pd.DataFrame)
    assert len(data) == 1
    assert data.loc[0, "name"] == "Test User"
    assert data.loc[0, "score"] == 7