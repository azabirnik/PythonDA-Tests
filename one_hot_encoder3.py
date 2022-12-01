from one_hot_encoder import fit_transform
from unittest import TestCase


class TestFitTrainsform(TestCase):
    def test_canonical_example(self):
        cities = ["Moscow", "New York", "Moscow", "London"]
        actual = fit_transform(cities)
        expected = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_long_input1(self):
        self.assertEqual(fit_transform(["A" * 100000]), [("A" * 10000, [1])])

    def test_long_input2(self):
        self.assertEqual(fit_transform(["A"] * 10000), [("A", [1])] * 10000)

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            fit_transform(1)
        with self.assertRaises(TypeError):
            fit_transform()
