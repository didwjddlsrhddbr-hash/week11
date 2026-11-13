import pytest

from bug3_logic import find_max


@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        ([70, 85, 60, 95], 95),
        ([95, 85, 70, 60], 95),
        ([10, 20, 30], 30),
    ],
)
def test_find_max_returns_largest_score(scores, expected):
    assert find_max(scores) == expected


def test_find_max_with_single_score():
    assert find_max([42]) == 42


def test_find_max_with_negative_scores():
    assert find_max([-8, -3, -12]) == -3
