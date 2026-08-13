import io
import unittest
from contextlib import redirect_stdout

from tonal import data


class CelloGuideTests(unittest.TestCase):
    def test_cello_guide_has_beginner_home_position_content(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            data.cello_guide()

        output = buffer.getvalue().lower()
        self.assertIn("home position", output)
        self.assertIn("first position", output)
        self.assertIn("open strings", output)
        self.assertIn("sheet music", output)
        self.assertIn("bass", output)


if __name__ == "__main__":
    unittest.main()
