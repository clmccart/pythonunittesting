import unittest
from tennis.tennis import tennis_score

test_case_data = {
    "even_scores":                      [("Love-All", 0,0),
                                        ("Fifteen-All", 1,1),
                                        ("Thirty-All", 2,2)],
    "early_games_with_uneven_scores":   [("Love-Fifteen", 0,1),
                                        ("Fifteen-Love", 1,0),
                                        ("Thirty-Fifteen", 2,1),
                                        ("Forty-Thirty", 3,2)]
}

class TennisTest(unittest.TestCase):

    def test_even_scores_zero_points(self):
        self.assert_tennis_score("Love-All", 0, 0)
    
    def test_even_scores_one_point(self):
        self.assert_tennis_score("Fifteen-All", 1, 1)
    
    def test_even_scores_two_points(self):
        self.assert_tennis_score("Thirty-All", 2, 2)

    def assert_tennis_score(self, expected_score, player1_points, player2_points):
        self.assertEqual(expected_score, tennis_score(player1_points, player2_points))

    def test_even_scores_early_game_multiple_asserts(self):
        self.assert_tennis_score("Love-All", 0, 0)
        self.assert_tennis_score("Fifteen-All", 1, 1)
        self.assert_tennis_score("Thirty-All", 2, 2)

    def test_uneven_scores_early_game_multiple_asserts(self):
        self.assert_tennis_score("Love-Fifteen", 0, 1)
        self.assert_tennis_score("Fifteen-Love", 1, 0)
        self.assert_tennis_score("Love-Thirty", 0, 2)
        self.assert_tennis_score("Forty-Thirty", 3, 2)
        

def tennis_test_template(*args):
    def foo(self):
        self.assert_tennis_score(*args)
    return foo 

for behaviour, test_cases in test_case_data.items():
    for tennis_test_case_data in test_cases:
        expected_output, player1_score, player2_score = tennis_test_case_data
        test_name = "test_monkeypatch_{0}_{1}_{2}".format(behaviour, player1_score, player2_score)
        tennis_test_case = tennis_test_template(*tennis_test_case_data)
        setattr(TennisTest, test_name, tennis_test_case)