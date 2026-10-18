
import unittest

from fasta_analyzer import sequence_analyzer, find_motif


class TestFastaAnalyzer(unittest.TestCase):

    def test_sequence_length(self):
        result = sequence_analyzer("ATGC")
        self.assertEqual(result["length"], 4)

    def test_gc_percentage(self):
        result = sequence_analyzer("ATGC")
        self.assertEqual(result["gc_percent"], 50.0)

    def test_at_percentage(self):
        result = sequence_analyzer("ATGC")
        self.assertEqual(result["at_percent"], 50.0)

    def test_find_motif(self):
        positions = find_motif("ATGCGATG", "ATG")
        self.assertEqual(positions, [1, 6])

    def test_overlapping_motif(self):
        positions = find_motif("ATATATA", "ATA")
        self.assertEqual(positions, [1, 3, 5])

    def test_empty_sequence(self):
        result = sequence_analyzer("")
        self.assertEqual(result["length"], 0)
        self.assertEqual(result["gc_percent"], 0.0)
        self.assertEqual(result["at_percent"], 0.0)

    def test_empty_motif(self):
        positions = find_motif("ATGC", "")
        self.assertEqual(positions, [])


if __name__ == "__main__":
    unittest.main()
