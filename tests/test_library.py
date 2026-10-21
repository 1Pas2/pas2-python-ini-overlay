import unittest
import pas2_ini_overlay as api


class Tests(unittest.TestCase):
    def test_override(self):
        self.assertEqual(
            api.overlay("[db]\nport=1\nhost=x", "[db]\nport=2"),
            {"db": {"port": "2", "host": "x"}},
        )

    def test_literal_and_case(self):
        self.assertEqual(
            api.overlay("[a]\nURL=100%\nurl=x")["a"], {"URL": "100%", "url": "x"}
        )

    def test_duplicate_rejected(self):
        from configparser import DuplicateOptionError

        with self.assertRaises(DuplicateOptionError):
            api.overlay("[a]\nx=1\nx=2")


if __name__ == "__main__":
    unittest.main()
