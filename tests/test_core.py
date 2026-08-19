import io
import unittest
from contextlib import redirect_stdout

from musor.cli import main
from musor.data import key_signature_staff, normalize_key_name, scale_from_key, transpose_key
from musor.quiz import answer_is_correct


class MusorCoreTests(unittest.TestCase):
    def test_main_help_displays_usage(self):
        stream = io.StringIO()
        with redirect_stdout(stream):
            main("--help")
        output = stream.getvalue()
        self.assertIn("Usage: musor <command> [arguments]", output)
        self.assertIn("quiz", output)

    def test_normalize_key_name_accepts_common_variants(self):
        self.assertEqual(normalize_key_name("A minor"), "A")
        self.assertEqual(normalize_key_name("Bb major"), "B♭")
        self.assertEqual(normalize_key_name("F#"), "F#")
        self.assertEqual(normalize_key_name("C major"), "C")

    def test_scale_from_key_lists_expected_notes(self):
        stream = io.StringIO()
        with redirect_stdout(stream):
            scale_from_key("G")
        output = stream.getvalue()
        self.assertIn("G major", output)
        self.assertIn("G A B C D E F# G", output)

    def test_transpose_key_reports_interval_and_target(self):
        stream = io.StringIO()
        with redirect_stdout(stream):
            transpose_key("C", "G")
        output = stream.getvalue()
        self.assertIn("perfect fifth", output)
        self.assertIn("Transposed scale", output)
        self.assertIn("G A B C D E F#", output)

    def test_quiz_answer_matching_allows_equivalent_inputs(self):
        self.assertTrue(answer_is_correct("4 sharps", "4", "How many sharps are in E major?"))
        self.assertTrue(answer_is_correct("B♭ E♭", "Bb Eb", "Which notes are flat in B♭ major?"))
        self.assertTrue(answer_is_correct("C", "C", "What is the relative major key for A minor?"))
        self.assertTrue(answer_is_correct("G", "G", "What is the relative major of E minor?"))

    def test_key_signature_staff_draws_valid_key_signature(self):
        staff = key_signature_staff("G major")
        self.assertIn("Key signature staff for G major", staff)
        self.assertIn("-", staff)


if __name__ == "__main__":
    unittest.main()
