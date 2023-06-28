import pytest
from py_project.common import detect_palindrome


@pytest.mark.parametrize(
    "text, expected_result",
    [("123321", True), ("abc", False), ("abc1cba", True), ("a", True)],
)
def test_detect_palindrome(text, expected_result):
    assert detect_palindrome(text) == expected_result
