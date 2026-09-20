from vec import Vec
import timeit
import numpy as np


# ==========================================
# Q6 / Q7
# Custom Vec performance
# ==========================================

sizes = [2000, 4000, 8000, 16000, 32000, 64000]


print("CUSTOM VEC PERFORMANCE")
    


for n in sizes:

    v1 = Vec.ones(n)
    v2 = Vec.ones(n)

    print("\nVector size:", n)

    # Addition
    t = timeit.timeit(
        lambda: v1 + v2,
        number=10
    )
    print("Addition:", t)

    # Subtraction
    t = timeit.timeit(
        lambda: v1 - v2,
        number=10
    )
    print("Subtraction:", t)

    # Scalar multiplication
    t = timeit.timeit(
        lambda: 2 * v1,
        number=10
    )
    print("Scalar multiplication:", t)

    # Negation
    t = timeit.timeit(
        lambda: -v1,
        number=10
    )
    print("Negation:", t)

    # Norm
    t = timeit.timeit(
        lambda: v1.norm(),
        number=10
    )
    print("Norm:", t)


# ==========================================
# Q8
# NumPy performance
# ==========================================

print("\n==========================================")
print("NUMPY PERFORMANCE")
print("==========================================")


for n in sizes:

    v1 = np.ones(n)
    v2 = np.ones(n)

    print("\nVector size:", n)

    # Addition
    t = timeit.timeit(
        lambda: v1 + v2,
        number=10
    )
    print("NumPy Addition:", t)

    # Subtraction
    t = timeit.timeit(
        lambda: v1 - v2,
        number=10
    )
    print("NumPy Subtraction:", t)

    # Scalar multiplication
    t = timeit.timeit(
        lambda: 2 * v1,
        number=10
    )
    print("NumPy Scalar multiplication:", t)

    # Negation
    t = timeit.timeit(
        lambda: -v1,
        number=10
    )
    print("NumPy Negation:", t)

    # Norm
    t = timeit.timeit(
        lambda: np.linalg.norm(v1),
        number=10
    )
    print("NumPy Norm:", t)