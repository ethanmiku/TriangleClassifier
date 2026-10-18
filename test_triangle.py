import math
import pytest
from triangle import is_triangle_valid, classify_triangle

# Test that a triagle with sidies 3, 4 , 5 is classified as Right Scalene
def test_right_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"

# Test that a triangle with sides 1 , 2 , 3 is classified as Invalid
def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"

# Test that a triangle with sides 5, 5, 5 is classified as Equilateral
def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"

# Test that a triangle with sides 5, 5, 8 is classified as Isosceles
def test_isosceles_triangle():
    assert classify_triangle(5, 5, 8) == "Isosceles"

# Test that a triangle with sides 5, 6, 7 is classified as Scalene
def test_scalene_triangle():
    assert classify_triangle(5, 6, 7) == "Scalene"

# Test that sides 5, 5, and 5 * sqrt(2) is classified as Right Isosceles
def test_right_isosceles_triangle():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"