# Lowest Common Ancestor

Data structure to find the lowest common ancestor of two nodes in a tree.

## \_\_init\_\_

### arguments

- `G: list[list[int]]`: adjacency list of the tree
- `root: int = 0`: root of the tree

### complexities

- Time: $O(n \log n)$
- Space: $O(n \log n)$

## lca

Returns the lowest common ancestor of two nodes `u` and `v`.

### arguments

- `u: int`: node
- `v: int`: node

### return value

- `int`: lowest common ancestor of `u` and `v`

### complexities

- $O(\log n)$