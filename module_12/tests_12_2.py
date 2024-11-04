import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == self.nick)

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == self.nick)

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == self.nick)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print("{" + ", ".join([f"{k}: {v}" for k, v in value.items()]) + "}")

if __name__ == '__main__':
    unittest.main()