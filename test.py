import sys
import os

sys.path.append(os.path.dirname(__file__))
import unittest
from unittest.mock import patch
import brainbuster


class TestQuiz(unittest.TestCase):

    # ✅ richtige Antwort
    @patch("builtins.input", return_value="4")
    def test_richtig(self, mock_input):
        frage = {"frage": "2+2?", "antwort": "4"}
        ergebnis = brainbuster.stelle_frage(frage)
        self.assertEqual(ergebnis, 1)

    # ❌ falsche Antwort
    @patch("builtins.input", return_value="5")
    def test_falsch(self, mock_input):
        frage = {"frage": "2+2?", "antwort": "4"}
        ergebnis = brainbuster.stelle_frage(frage)
        self.assertEqual(ergebnis, 0)

    # ℹ️ Hilfe testen
    @patch("builtins.input", side_effect=["h", "4"])
    def test_hilfe(self, mock_input):
        frage = {"frage": "2+2?", "antwort": "4"}
        ergebnis = brainbuster.stelle_frage(frage)
        self.assertEqual(ergebnis, 1)


if __name__ == "__main__":
    unittest.main()