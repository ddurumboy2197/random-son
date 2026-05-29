# test_random_number.py
import pytest
import random

def test_random_number():
    random_number = random.randint(1, 100)
    assert 1 <= random_number <= 100
