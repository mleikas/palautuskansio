import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_etsi_tiimi(self):
        asf = self.statistics.team("PIT")
        self.assertEqual(str(asf[0]), str(Player("Lemieux", "PIT", 45, 54)))

    def test_etsi_pelaaja(self):
        asf = self.statistics.search("Semenko")
        self.assertEqual(str(asf), str(Player("Semenko", "EDM", 4, 12)))

    def test_etsi_vaara_pelaaja(self):
        asf = self.statistics.search("gabagool")
        self.assertEqual(asf, None)

    def test_etsi_top_pisteet(self):
        asf = self.statistics.top(2)
        self.assertEqual(str(asf[0]), str(Player("Gretzky", "EDM", 35, 89)))

    def test_etsi_top_maalit(self):
        asf = self.statistics.top(2,SortBy.GOALS)
        self.assertEqual(str(asf[0]), str(Player("Lemieux", "PIT", 45, 54)))

    def test_etsi_top_assistit(self):
        asf = self.statistics.top(2,SortBy.ASSISTS)
        self.assertEqual(str(asf[0]), str(Player("Gretzky", "EDM", 35, 89)))