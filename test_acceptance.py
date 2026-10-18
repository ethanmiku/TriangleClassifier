import math
from triangle import classify_triangle

def test_stained_glass_acceptance():

    # Criterion 1: Correctly classify valid triangles
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(5, 5, 8) == "Isosceles"
    assert classify_triangle(4, 5, 7) == "Scalene"

    # Criterion 2: Reject invalid traingles without crashing
    assert classify_triangle(0, 5, 5) == "Invalid"
    assert classify_triangle(-1, 5, 5) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"

    #Criterion 3: Identify right triangles needing reinforced corners
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"

    # Verify that non right triangles are not flagged
    assert classify_triangle(4, 5, 7) == "Scalene"


