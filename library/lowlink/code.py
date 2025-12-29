def lowlink(n, E):
    m = len(E)
    G = [[] for _ in range(n)]
    for i, (u, v) in enumerate(E):
        G[u].append((v, i))
        G[v].append((u, i))

    INF = 1 << 60
    dp = [INF] * n
    is_bridge = [False] * m
    for v in range(n):
        if dp[v] != INF:
            continue
        stack = [(v, -1, -1)]
        while stack:
            v, p, i = stack.pop()
            if v >= 0:
                if dp[v] != INF:
                    stack.pop()
                    continue
                dp[v] = 0
                for nv, ni in G[v]:
                    if dp[nv] == INF:
                        stack.append((~nv, v, ni))
                        stack.append((nv, v, ni))
                    elif ni != i:
                        dp[v] += 1
                        dp[nv] -= 1
            else:
                v = ~v
                is_bridge[i] = dp[v] == 0
                dp[p] += dp[v]

    return G, is_bridge

if __name__ == "__main__":
    n = 5
    E = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)]
    G, is_bridge = lowlink(n, E)
    print(is_bridge)