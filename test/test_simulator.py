from unittest import TestCase
from src.simulator import simulator


class TestSimulator(TestCase):

    def test_simulator(self):
        self.assertEqual(simulator(1, 2, 3), 6)