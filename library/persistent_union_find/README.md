# Persistent Union Find

Fully persistent data structure that supports:

- edge addition: connect two vertices
- connectivity detection: determine whether two vertices are in the same connected component
- persistence: access past version of the data structure

## \_\_init\_\_

### arguments

- `n: int`: number of vertices

### complexities

- Time: $O(n)$
- Space: $O(n)$

## root

Returns the representative of the connected component containing vertex `k`. While rarely used directly, this method can be used to determine if two vertices belong to the same component.

### arguments

- `k: int`: vertex

### returns

- `int`: representative of the connected component containing vertex `k`

### complexities

- $O(\log n)$

## unite

Add an edge spanning between vertices `i` and `j`.

### arguments

- `i: int`: vertex
- `j: int`: vertex

### returns

- `PersistentUnionFind`: new version of the data structure

### complexities

- $O(\log n)$

## is_connected

Returns whether vertices `i` and `j` are connected.

### arguments

- `i: int`: vertex
- `j: int`: vertex

### returns

- `bool`: `True` if vertices `i` and `j` are connected, `False` otherwise

### complexities

- $O(\log n)$

## size

Returns the size of the connected component containing vertex `k`.

### arguments

- `k: int`: vertex

### returns

- `int`: size of the connected component containing vertex `k`

### complexities

- $O(\log n)$