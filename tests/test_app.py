"""Test greeting behavior without importing Gradio or starting its server."""

import pytest

from app import generate_message


def test_english_name():
    assert generate_message("Alice") == (
        "Hello, Alice! CI/CD deployment is working successfully."
    )


def test_korean_name():
    assert generate_message("홍길동") == (
        "Hello, 홍길동! CI/CD deployment is working successfully."
    )


def test_empty_input():
    assert generate_message("") == "Please enter your name."


@pytest.mark.parametrize("name", [" ", "\t\n", "\u3000"])
def test_whitespace_only_input(name):
    assert generate_message(name) == "Please enter your name."


def test_missing_input():
    assert generate_message(None) == "Please enter your name."


def test_trims_surrounding_whitespace():
    assert generate_message("  Alice \n") == (
        "Hello, Alice! CI/CD deployment is working successfully."
    )


def test_preserves_spaces_inside_name():
    assert generate_message("Ada Lovelace") == (
        "Hello, Ada Lovelace! CI/CD deployment is working successfully."
    )
