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