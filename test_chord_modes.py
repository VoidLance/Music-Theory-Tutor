import io
import unittest
from contextlib import redirect_stdout

from tonal.cli import FUNCTIONS
from tonal.data import (
    chord_from_key,
    modes_from_key,
    scales_overview,
    chords_overview,
    circle_of_fifths,
    riff_guide,
    bassline_guide,
    melody_guide,
    genre_analysis_guide,
    walking_bassline_guide,
)
from tonal.quiz import scale_quiz, chord_quiz, modes_quiz, combined_quiz


class ChordAndModesTest(unittest.TestCase):
    def test_chord_building_explains_method(self):
        buf = io.StringIO()

        with redirect_stdout(buf):
            chord_from_key("G")

        output = buf.getvalue().lower()

        self.assertIn("g major", output)
        self.assertIn("g b d", output)
        self.assertIn("stack", output)

    def test_modes_from_key(self):
        buf = io.StringIO()

        with redirect_stdout(buf):
            modes_from_key("C")

        output = buf.getvalue().lower()

        self.assertIn("ionian", output)
        self.assertIn("dorian", output)
        self.assertIn("c d e f g a b c", output)

    def test_generic_overview_commands_exist(self):
        self.assertIn("scales", FUNCTIONS)
        self.assertIn("chords", FUNCTIONS)
        self.assertIn("modes", FUNCTIONS)

        buf = io.StringIO()
        with redirect_stdout(buf):
            scales_overview()
        output = buf.getvalue().lower()
        self.assertIn("major scale", output)
        self.assertIn("key signature", output)

        buf = io.StringIO()
        with redirect_stdout(buf):
            chords_overview()
        output = buf.getvalue().lower()
        self.assertIn("triad", output)
        self.assertIn("1st", output)

    def test_modes_include_quality_and_feeling(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            modes_from_key("C")
        output = buf.getvalue().lower()

        self.assertIn("dorian", output)
        self.assertIn("minor", output)
        self.assertIn("major", output)
        self.assertIn("soulful", output)
        self.assertIn("bright", output)

    def test_explicit_minor_mode_request_stays_minor(self):
        for value in ["B♭ minor", "Bb minor", "b flat minor"]:
            buf = io.StringIO()
            with redirect_stdout(buf):
                modes_from_key(value)
            output = buf.getvalue().lower()

            self.assertIn("minor", output)
            self.assertNotIn("b♭ major", output)
            self.assertNotIn("bb major", output)

    def test_topic_specific_and_combined_quiz_functions_exist(self):
        for quiz_fn in [scale_quiz, chord_quiz, modes_quiz, combined_quiz]:
            self.assertTrue(callable(quiz_fn))

    def test_circle_relationships_explain_distance_and_quality(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            circle_of_fifths()
        output = buf.getvalue().lower()

        self.assertIn("close relationship", output)
        self.assertIn("distant relationship", output)
        self.assertIn("tonal quality", output)
        self.assertIn("stable", output)
        self.assertIn("dramatic", output)

    def test_practical_music_construction_guides_exist(self):
        for guide in [riff_guide, bassline_guide, melody_guide, genre_analysis_guide, walking_bassline_guide]:
            self.assertTrue(callable(guide))

        buf = io.StringIO()
        with redirect_stdout(buf):
            bassline_guide()
        output = buf.getvalue().lower()
        self.assertIn("walking bassline", output)
        self.assertIn("root", output)

        buf = io.StringIO()
        with redirect_stdout(buf):
            genre_analysis_guide()
        output = buf.getvalue().lower()
        self.assertIn("genre", output)
        self.assertIn("rhythm", output)


if __name__ == "__main__":
    unittest.main()
