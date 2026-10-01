import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_names(self):
        for name, expected in (
            ("", "Hello, friend!"),
            ("   ", "Hello, friend!"),
            ("\t\n", "Hello, friend!"),
            (" Ada ", "Hello, Ada!"),
            ("Ada", "Hello, Ada!"),
        ):
            with self.subTest(name=name):
                self.assertEqual(greet(name), expected)


if __name__ == "__main__":
    unittest.main()
