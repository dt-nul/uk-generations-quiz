from validation import validate_name


def test_valid_name():
    """Test that a normal participant name is accepted."""
    assert validate_name("Daniel Tyreman") is True


def test_empty_name():
    """Test that an empty participant name is rejected."""
    assert validate_name("") is False


def test_name_with_numbers():
    """Test that a participant name containing numbers is rejected."""
    assert validate_name("Daniel123") is False