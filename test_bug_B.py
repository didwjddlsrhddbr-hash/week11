from bug3_logic import find_max


def test_find_max_returns_largest_score():
    assert find_max([12, 7, 25, 18]) == 25


def test_find_max_when_largest_score_is_last():
    assert find_max([70, 85, 60, 95]) == 95


def test_find_max_with_single_score():
    assert find_max([42]) == 42


def test_find_max_with_negative_scores():
    assert find_max([-8, -3, -12]) == -3
