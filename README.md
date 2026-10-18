# Triangle Classifier

A Python program that validates and classifies triangles based on three side lengths. The project uses pytest for automated unit testing and GitHub Copilot to assist with test generation.

## Features

- Validates triangle side lengths using the triangle inequality.
- Rejects triangles with zero or negative side lengths.
- Classifies triangles as Equilateral, Isosceles, or Scalene.
- Identifies right triangles using the Pythagorean theorem with a floating-point tolerance.
- Handles edge cases involving very small side lengths and nearly degenerate triangles.

## Project Structure

- `triangle.py` — Triangle validation and classification functions.
- `test_triangle.py` — Unit tests written with GitHub Copilot assistance.
- `test_acceptance.py` — Customer acceptance test.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation.

## How to Run the Tests

Make sure Python is installed.

**1. Install dependencies**

`py -m pip install -r requirements.txt`

**2. Run all tests**

`py -m pytest -v`

**3. Run unit tests only**

`py -m pytest test_triangle.py -v`

**4. Run acceptance tests only**

`py -m pytest test_acceptance.py -v`

The unit test suite currently contains 14 passing tests.

## Equivalence Classes and Boundary Cases

The following equivalence classes and boundary conditions were identified and tested:

| Category | Example Input | Expected Result |
|---|---|---|
| Equilateral | (5, 5, 5) | Equilateral |
| Isosceles | (5, 5, 8) | Isosceles |
| Scalene | (5, 6, 7) | Scalene |
| Right Scalene | (3, 4, 5) | Right Scalene |
| Right Isosceles | (5, 5, 5√2) | Right Isosceles |
| Invalid (triangle inequality) | (1, 2, 3) | Invalid |
| Invalid (zero side) | (0, 5, 5) | Invalid |
| Invalid (negative side) | (-1, 5, 5) | Invalid |
| Nearly right triangle | (3, 4, 5.0001) | Scalene |
| Very small equilateral | (1e-10, 1e-10, 1e-10) | Equilateral |
| Nearly degenerate | (1, 1, 1.9999999999) | Isosceles |

### Why an Equilateral Triangle Cannot Be Right

An equilateral triangle has three equal angles of 60 degrees. Since a right triangle must have one 90-degree angle, an equilateral triangle cannot also be a right triangle.

## GitHub Copilot Review Log

GitHub Copilot was used to suggest unit tests. Each suggestion was reviewed against the triangle classification requirements before being accepted or edited.

| Test | Copilot-suggested? | Decision | Why |
|---|---|---|---|
| `test_right_scalene` | Yes | Kept | Correctly classified (3, 4, 5) as Right Scalene. |
| `test_invalid_triangle` | Yes | Kept | Correctly rejected a degenerate triangle. |
| `test_equilateral_triangle` | Yes | Kept | Correctly verified three equal sides. |
| `test_isosceles_triangle` | Yes | Kept | Correctly verified exactly two equal sides. |
| `test_scalene_triangle` | Yes | Kept | Correctly classified (5, 6, 7) as Scalene. |
| `test_right_isosceles_triangle` | Yes | Kept | Correctly checked a right-isosceles triangle using √2. |
| `test_zero_length_side` | Yes | Kept | Correctly rejected a zero-length side. |
| `test_negative_length_side` | Yes | Kept | Correctly rejected a negative side length. |
| `test_is_valid_triangle` | Yes | Kept | Correctly checked multiple valid and invalid triangles. |
| `test_almost_right_triangle` | Yes | Kept | Correctly distinguished a nearly right triangle from a right triangle. |
| `test_floating_point_precision` | Yes | Kept | Correctly checked a right-isosceles triangle using a floating-point value. |
| `test_triangle_inequality_boundary` | Yes | Kept | Correctly rejected triangles where two sides sum to exactly the third. |
| `test_small_equilateral_triangle` | Yes | Kept | Correct test that exposed a precision bug in the original implementation. |
| `test_nearly_degenerate_triangle` | Yes | **Edited** | Copilot incorrectly expected Invalid for valid triangles with sides very close to the triangle inequality boundary. |

### Copilot Mistake Identified and Corrected

When generating `test_nearly_degenerate_triangle`, Copilot suggested that triangles with sides (1, 1, 1.9999999999), (1, 1, 1.999999999), and (1, 1, 1.99999999) should be classified as `"Invalid"`.

I checked these values against the triangle inequality and determined that all three are valid because the sum of the first two sides is strictly greater than the third.

Since exactly two sides are equal, the correct classification is `"Isosceles"`.

I edited the suggested assertions to use the correct expected output and verified the correction using pytest.

### Additional Bug Found Through Testing

A Copilot-generated test involving very small equal side lengths exposed a bug in the original implementation.

The initial Pythagorean check used `math.isclose()` with an absolute tolerance that was too large for extremely small triangles. This caused a small equilateral triangle to be incorrectly classified as a right triangle.

The implementation was corrected by normalizing the side lengths before applying the floating-point tolerance.

After the correction, all 13 existing tests passed. An additional near-degenerate triangle test was then added and corrected, bringing the unit test total to 14 passing tests.

## Customer Acceptance Criteria

1. Triangle Classification
When a customer enters three side lengths that form a valid triangle, the program must correctly identify the shape as "Equilateral", "Isosceles", or "Scalene". For example, entering (5, 5, 5) should return "Equilateral", confirming that the triangle is buildable.

2. Invalid Triangle Handling
If a customer enters side lengths that cannot form a valid triangle, the program must return "Invalid" without crashing. This includes zero or negative side lengths and cases where the sum of two sides is less than or equal to the third. For example, entering (1, 2, 3) should return "Invalid".

3. Right Triangle Identification
When a customer enters side lengths that form a right triangle, the program must include "Right" in the classification so the studio knows the piece needs reinforced corners. For example, entering (3, 4, 5) should return "Right Scalene". Triangles without a right angle must not receive the "Right" prefix.

## AI-Use Disclosure

**GitHub Copilot:** Used to generate suggestions for unit tests, including standard triangle classifications, invalid inputs, and floating-point edge cases. Suggestions were reviewed, verified, and corrected where necessary.

**ChatGPT:** Used for guidance on Python implementation, floating-point tolerance, and README documentation. Generated code and explanations were checked through testing and review.
