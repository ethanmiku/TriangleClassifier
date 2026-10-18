import math

def is_valid_triangle(a,b,c) -> bool:
    # All sides must be greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False

    #The sum of any two sides must be greater than the third
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True

def classify_triangle(a,b,c) -> str:
    #check if the triangle is valid first
    if not is_valid_triangle(a,b,c):
        return "Invalid"

    #determine the triangle type
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    #sort the sides so the largewst is the hypotenuse
    sides = sorted([a,b,c])
    x, y, z = sides

    #check the pythagorean theorm using a tolerance

    if math.isclose((x / z)**2 + (y / z)**2, 1.0, rel_tol = 1e-9, abs_tol = 1e-9):
        return "Right " + triangle_type

    return triangle_type
    


