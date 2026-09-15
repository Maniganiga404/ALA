from vec import Vec


# -----------------------------------
# Vector creation and length
# -----------------------------------

v = Vec([1, 2, 3])

assert v.elements == [1, 2, 3]
assert len(v) == 3

print("Vector creation and length tests passed!")


# -----------------------------------
# Addition
# -----------------------------------

v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])

v3 = v1 + v2

print("Addition:", v3)

assert v3.elements == [5, 7, 9]

print("Addition test passed!")


# -----------------------------------
# Subtraction
# -----------------------------------

v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])

v3 = v1 - v2

print("Subtraction:", v3)

assert v3.elements == [-3, -3, -3]

print("Subtraction test passed!")


# -----------------------------------
# Scalar multiplication
# -----------------------------------

v1 = Vec([1, 2, 3])

v3 = 2 * v1

print("Multiplication:", v3)

assert v3.elements == [2, 4, 6]

print("Multiplication test passed!")


# -----------------------------------
# Negation
# -----------------------------------

v3 = -v1

print("Negation:", v3)

assert v3.elements == [-1, -2, -3]

print("Negation test passed!")


# -----------------------------------
# Scalar addition
# -----------------------------------

v3 = 5 + v1

print("Scalar Addition:", v3)

assert v3.elements == [6, 7, 8]

print("Scalar Addition test passed!")


# -----------------------------------
# In-place addition
# -----------------------------------

v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])

v1 += v2

print("In-place Addition:", v1)

assert v1.elements == [5, 7, 9]

print("In-place Addition test passed!")


# -----------------------------------
# In-place multiplication
# -----------------------------------

v1 = Vec([1, 2, 3])

v1 *= 2

print("In-place Multiplication:", v1)

assert v1.elements == [2, 4, 6]

print("In-place Multiplication test passed!")


# -----------------------------------
# Zeros
# -----------------------------------

v1 = Vec.zeros(5)

print("Zeros:", v1)

assert v1.elements == [
    0.0, 0.0, 0.0, 0.0, 0.0
]

print("Zeros test passed!")


# -----------------------------------
# Ones
# -----------------------------------

v1 = Vec.ones(5)

print("Ones:", v1)

assert v1.elements == [
    1.0, 1.0, 1.0, 1.0, 1.0
]

print("Ones test passed!")


# -----------------------------------
# Uniform
# -----------------------------------

v = Vec.uniform(5)

print("Uniform:", v)

assert len(v) == 5
assert all(0 <= x <= 1 for x in v.elements)

print("Uniform test passed!")


# -----------------------------------
# Norm
# -----------------------------------

v = Vec([3, 4])

print("Norm:", v.norm())

assert v.norm() == 5.0

print("Norm test passed!")


print("\nAll tests passed!")