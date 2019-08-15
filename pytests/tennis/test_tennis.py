from pytests.tennis.tennis import tennis_score
import pytest

examples = (("expected_score", "player1_points", "player2_points"), 
[
("Love-All", 0, 0),
("Fifteen-All", 1, 1),
("Thirty-All", 2, 2),
("Love-Fifteen", 0, 1),
("Fifteen-Love", 1, 0),
("Thirty-Fifteen", 2, 1),
("Forty-Thirty", 3, 2),
("Advantage Player 1", 4, 3),
("Advantage Player 2", 3, 4),
("Advantage Player 1", 23, 22),
("Deuce", 3, 3),
("Deuce", 4, 4),
("Deuce", 14, 14),
("Win for Player 1", 4, 0),
("Win for Player 2", 1, 4),
("Win for Player 1", 6, 4)
])

@pytest.mark.parametrize(*examples)
def test_early_game_scores_equal(expected_score, player1_points, player2_points):
    assert expected_score == tennis_score(player1_points, player2_points)
