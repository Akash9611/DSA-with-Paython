# DSA With Python

# Arithmetic Operations in Python

## Explanation of Operations
1. **Addition (`+`)**: Adds two numbers.
2. **Subtraction (`-`)**: Subtracts the second number from the first.
3. **Multiplication (`*`)**: Multiplies two numbers.
4. **Division (`/`)**: Divides the first number by the second, returning a floating-point result.
5. **Modulus (`%`)**: Returns the remainder of the division.
6. **Exponentiation (`**`)**: Raises the first number to the power of the second.
7. **Floor Division (`//`)**: Performs division and rounds the result down to the nearest integer.

## Notes
- When using floor division (`//`), the result is always rounded down.
- If one of the numbers is negative in floor division, the result is also negative.
- Exponentiation is useful for calculating powers of numbers.

# Bitwise Operations in Python

## Explanation of Bitwise Operations
1. **AND (`&`)**: Performs a binary AND operation between two numbers.
2. **OR (`|`)**: Performs a binary OR operation between two numbers.
3. **XOR (`^`)**: Performs a binary XOR operation between two numbers.
4. **COMPLEMENT (`~`)**: Flips all bits of the number.
5. **LEFT SHIFT (`<<`)**: Moves the bits of a number to the left by a specified number of places.
6. **RIGHT SHIFT (`>>`)**: Moves the bits of a number to the right by a specified number of places.

### note-
Ex- bin(c): This function converts the integer c to its binary string representation (e.g., '0b110101'). 
---

# Additional Information

## Understanding Bitwise Operations
- **AND (`&`)**: Compares each bit of two numbers and returns `1` if both bits are `1`, otherwise `0`.
- **OR (`|`)**: Compares each bit and returns `1` if at least one of the bits is `1`.
- **XOR (`^`)**: Compares each bit and returns `1` if the bits are different, otherwise `0`.
- **COMPLEMENT (`~`)**: Inverts all bits of the number (two's complement representation).
- **LEFT SHIFT (`<<`)**: Shifting left effectively multiplies the number by `2^n`, where `n` is the shift amount.
- **RIGHT SHIFT (`>>`)**: Shifting right effectively divides the number by `2^n`, rounding down.

## Example Interpretation
- If `a = 10 (1010 in binary)`, `b = 12 (1100 in binary)`, then:
  - `a & b` results in `1000 (8 in decimal)`.
  - `a | b` results in `1110 (14 in decimal)`.
  - `a ^ b` results in `0110 (6 in decimal)`.
  - `~a` results in the two's complement of `10`, which is `-11`.
  - `a << b` shifts `a` left by `b` bits, resulting in a much larger value.
  - `a >> b` shifts `a` right by `b` bits, reducing its value significantly.




