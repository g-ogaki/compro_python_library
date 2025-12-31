# Max Flow

Solves maximum flow problem.

## \_\_init\_\_

### Arguments

- `n: int`: number of nodes

## add_edge

Appends an edge with capacity to the graph.

### Arguments

- `u: int`: from node
- `v: int`: to node
- `cap: int`: capacity

## solve

Finds the maximum flow from the source to the sink.

### Arguments

- `s: int`: source node
- `t: int`: sink node

### Returns

- `int`: maximum flow

### Complexities

$$
\begin{cases}
O(\min(n^{2/3}m, m^{3/2})) & \text{if graph is unit capacity (i.e., all capacities are the same)} \\
O(n^2m) & \text{otherwise}
\end{cases}
$$

where $m$ represents the number of edges added.