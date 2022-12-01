"""Tests for Morse Code Translator"""

import pytest
from one_hot_encoder import fit_transform


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ["Moscow", "New York", "Moscow", "London"],
            [
                ("Moscow", [0, 0, 1]),
                ("New York", [0, 1, 0]),
                ("Moscow", [0, 0, 1]),
                ("London", [1, 0, 0]),
            ],
        ),
        (["A" * 10000], [("A" * 10000, [1])]),
        (["A"] * 10000, [("A", [1])] * 10000),
    ],
)
def test_eval(test_input, expected):
    assert fit_transform(test_input) == expected


def test_wrong_input():
    with pytest.raises(TypeError):
        fit_transform(1)
    with pytest.raises(TypeError):
        fit_transform()


if __name__ == "__main__":
    pass
