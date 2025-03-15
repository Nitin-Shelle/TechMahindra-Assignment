import pytest
import pandas as pd
from main import classify_player  # Import function from main.py (if applicable)

# Sample test data
test_data = [
    {"runs": 600, "wickets": 60, "expected": "All-Rounder"},
    {"runs": 700, "wickets": 10, "expected": "Batsman"},
    {"runs": 400, "wickets": 30, "expected": "Bowler"},
]

@pytest.mark.parametrize("data", test_data)
def test_classify_player(data):
    assert classify_player(data["runs"], data["wickets"]) == data["expected"]

def test_output_file_exists():
    """Check if the output CSV file is generated."""
    df = pd.read_csv("test_result.csv")
    assert not df.empty, "Output file is empty!"
