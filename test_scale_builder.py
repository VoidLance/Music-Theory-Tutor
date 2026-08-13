import io
import unittest
from contextlib import redirect_stdout

from tonal.data import scale_from_key


class ScaleBuilderTest(unittest.TestCase):
    def test_major_scale_from_key_signature(self):
        buf = io.StringIO()

        with redirect_stdout(buf):
            scale_from_key("G")

        output = buf.getvalue()

        self.assertIn("G major", output)
        self.assertIn("G A B C D E F# G", output)
        self.assertIn("F#", output)

    def test_minor_scale_from_key_signature(self):
        buf = io.StringIO()

        with redirect_stdout(buf):
            scale_from_key("A minor")

        output = buf.getvalue()

        self.assertIn("A minor", output)
        self.assertIn("A B C D E F G A", output)


if __name__ == "__main__":
    unittest.main()
