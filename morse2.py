"""Tests for Morse Code Translator"""

import pytest
from morse import decode


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("... --- ...", "SOS"),
        (".--. -.-- - .... --- -.", "PYTHON"),
        (
            ".- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- "
            ".- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- "
            ".- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- "
            ".- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- "
            ".- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- "
            ".- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- "
            ".- .- .- .-",
            "A" * 100,
        ),
    ],
)
def test_eval(test_input, expected):
    assert decode(test_input) == expected


if __name__ == "__main__":
    pass
