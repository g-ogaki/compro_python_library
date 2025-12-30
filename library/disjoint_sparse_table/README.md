# Disjoint Sparse Table

Data structure for arrays of semi-groups that supports range queries.

## \_\_init\_\_

### arguments

- `A: list[T]`: array of the semi-group
- `dot: Callable[[T, T], T]`: binary operation of the semi-group

### complexities

- Time: $O(n \log n)$
- Space: $O(n \log n)$

## prod

Calculates the product of $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$.

### arguments

- `l: int`: left endpoint of the range (inclusive)
- `r: int`: right endpoint of the range (exclusive)

### return value

- `T`: $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$

### complexities

- $O(1)$