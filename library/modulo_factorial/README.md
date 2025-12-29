# Modulo Factorial

Calculates factorials and inverse factorials modulo a prime number $p$.

## \_\_init\_\_

### Arguments

- `N: int`: maximum number to calculate factorials and inverse factorials

### Complexities

- Time: $O(N + \log p)$
- Space: $O(N)$

## inv

Returns $n^{-1}$ modulo $p$.

### Arguments

- `n: int`: number to calculate the inverse of

### Returns

- `int`: $n^{-1}$ modulo $p$

### Complexities

$$
\begin{cases}
O(1) & \text{if $n \le N$,} \\
O(\log p) & \text{if $n > N$,}
\end{cases}
$$

## fact

Returns $n!$ modulo $p$.

### Arguments

- `n: int`: number to calculate the factorial of

### Returns

- `int`: $n!$ modulo $p$

### Complexities

- $O(1)$

## invfact

Returns $(n!)^{-1}$ modulo $p$.

### Arguments

- `n: int`: number to calculate the inverse factorial of

### Returns

- `int`: $(n!)^{-1}$ modulo $p$

### Complexities

- $O(1)$

## comb

Returns $\dbinom{n}{k} = \dfrac{n!}{k!(n-k)!}$ modulo $p$.

### Arguments

- `n: int`: number of elements
- `k: int`: number of elements to choose

### Returns

- `int`: $\dbinom{n}{k}$ modulo $p$

### Complexities

- $O(1)$

## perm

Returns $P(n, k) = \dfrac{n!}{(n-k)!}$ modulo $p$.

### Arguments

- `n: int`: number of elements
- `k: int`: number of elements to choose

### Returns

- `int`: $P(n, k)$ modulo $p$

### Complexities

- $O(1)$