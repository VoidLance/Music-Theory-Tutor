import io
import unittest
from contextlib import redirect_stdout

from tonal.data import circle_of_fifths


class CircleOfFifthsTest(unittest.TestCase):
    def test_circle_of_fifths_output_includes_reference_notes(self):
        buf = io.StringIO()

        with redirect_stdout(buf):
            circle_of_fifths()

        output = buf.getvalue()

        self.assertIn("Circle of Fifths", output)
        self.assertIn("C -> G -> D", output)
        self.assertIn("relative major", output.lower())
        self.assertIn("perfect fifth", output.lower())


if __name__ == "__main__":
    unittest.main()
