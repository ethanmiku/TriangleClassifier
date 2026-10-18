import math
import pytest
from triangle import is_valid_triangle, classify_triangle

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

# Test that a triangle wwith a zero-length side is classified as Invalid
def test_zero_length_side():
    assert classify_triangle(0, 5, 5) == "Invalid"

# Test that a triangle with a negative-length side is classified as Invalid
def test_negative_length_side():
    assert classify_triangle(-1, 5, 5) == "Invalid"

# Test that is_valid_triangle correctly identifies valid and invalid triangles
def test_is_valid_triangle():
    assert is_valid_triangle(3, 4, 5) == True
    assert is_valid_triangle(1, 2, 3) == False
    assert is_valid_triangle(5, 5, 5) == True
    assert is_valid_triangle(5, 5, 8) == True
    assert is_valid_triangle(5, 6, 7) == True
    assert is_valid_triangle(0, 5, 5) == False
    assert is_valid_triangle(-1, 5, 5) == False

# Test that sides 3,4, and 5.0001 form a Scalene triangle, not a Right Scalene triangle
def test_almost_right_triangle():
    assert classify_triangle(3, 4, 5.0001) == "Scalene"


# Generate tests for tricky triangle edge cases,
# including floating-point precision and triangle inequality boundaries.
# Verify that each test uses the correct expected result.

def test_floating_point_precision():
    assert classify_triangle(1.0, 1.0, 1.4142135623730951) == "Right Isosceles"

def test_triangle_inequality_boundary():
    assert classify_triangle(1, 1, 2) == "Invalid"
    assert classify_triangle(1, 2, 1) == "Invalid"
    assert classify_triangle(2, 1, 1) == "Invalid"

# Test that a triangle with three very small equal positive sides is classified correctly
def test_small_equilateral_triangle():
    assert classify_triangle(1e-10, 1e-10, 1e-10) == "Equilateral"

# Generate additional tests for tricky triangle boundary conditions.
# Include cases where sides are nearly degenerate or nearly right-angled.
# Determine the expected classifications independently.
def test_nearly_degenerate_triangle():
    assert classify_triangle(1, 1, 1.9999999999) == "Isosceles"
    assert classify_triangle(1, 1, 1.99999999999) == "Isosceles"
    assert classify_triangle(1, 1, 1.999999999999) == "Isosceles"