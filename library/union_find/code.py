class UnionFind(object):
    def __init__(self, n):
        self._par = [*range(n)]
        self._size = [1] * n

    def root(self, k):
        root = k
        while root != self._par[root]:
            root = self._par[root]
        while k != root:
            k, self._par[k] = self._par[k], root
        return root

    def unite(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j:
            return False
        if self._size[i] < self._size[j]:
            i, j = j, i
        self._par[j] = i
        self._size[i] += self._size[j]
        return True

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, k):
        return self._size[self.root(k)]

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.unite(0, 1)
    uf.unite(1, 2)
    print(uf.is_connected(0, 2))
    print(uf.is_connected(0, 3))
    print(uf.size(0))