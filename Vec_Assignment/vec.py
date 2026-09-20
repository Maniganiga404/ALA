import random
import math
from typing import Self


class Vec:
    """
    A custom vector class implementation for educational purposes.
    """

    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = []
        else:
            elements = list(src)

            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")

            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")

        if len(self.elements) != len(t):
            raise TypeError("Vectors must be of same dimensions")

        return Vec([
            round(x + y, 5)
            for x, y in zip(self.elements, t.elements)
        ])

    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(
                f"Vector multiplication with invalid type: {type(scalar)}"
            )

        return Vec([
            round(x * scalar, 5)
            for x in self.elements
        ])

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(
                f"Vector multiplication with invalid type: {type(scalar)}"
            )

        for i, val in enumerate(self.elements):
            self.elements[i] = round(val * scalar, 5)

        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")

        if len(self.elements) != len(t):
            raise TypeError("Vectors must be of same dimensions")

        return Vec([
            round(x - y, 5)
            for x, y in zip(self.elements, t.elements)
        ])

    def __neg__(self) -> Self:
        return Vec([-x for x in self.elements])

    def __radd__(self, other: int | float) -> Self:
        if not isinstance(other, (int, float)):
            raise TypeError(f"Expected number: {type(other)}")

        return Vec([
            other + x
            for x in self.elements
        ])

    def __iadd__(self, other: Self) -> Self:
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")

        if len(self.elements) != len(other):
            raise TypeError("Vectors must be of same dimensions")

        for i, val in enumerate(self.elements):
            self.elements[i] = round(
                val + other.elements[i], 5
            )

        return self

    @staticmethod
    def zeros(n: int) -> Self:
        if n <= 0:
            raise ValueError("n must be greater than 0")

        return Vec([0.0] * n)

    @staticmethod
    def ones(n: int) -> Self:
        if n <= 0:
            raise ValueError("n must be greater than 0")

        return Vec([1.0] * n)

    @staticmethod
    def uniform(n: int) -> Self:
        if n <= 0:
            raise ValueError("n must be greater than 0")

        return Vec([
            random.uniform(0, 1)
            for _ in range(n)
        ])

    def norm(self) -> float:
        if len(self.elements) == 0:
            raise ValueError("Vector cannot be empty")

        import math

        return math.sqrt(
            sum(x * x for x in self.elements)
        )

    #mean
    def mean(self) -> float:
        if len(self.elements) == 0:
            raise ValueError("Vector cannot be empty")

        return sum(self.elements) / len(self.elements)

    #demean
    def demean(self) -> self:
        if(len(self.elements) == 0):
            raise ValueError("Vector cannot be empty")

        mean = self.mean()

        return Vec([x - mean for x in self.elements])

    #standard deviation
    def std(self) -> float:
        if(len(self.elements) == 0):
            raise ValueError("vector cannot be empty")

        de_meaned =self.demean()

        return math.sqrt(sum(x * x for x in de_meaned.elements)/len(de_meaned.elements))