MOD = 998244353

class ModFact(object):
    def __init__(self, N):
        fact, invfact = [1] * (N + 1), [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = i * fact[i - 1] % MOD
        invfact[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD
        self._fact, self._invfact = fact, invfact

    def inv(self, n):
        return self._fact[n - 1] * self._invfact[n] % MOD if n < len(self._fact) else pow(n, MOD - 2, MOD)

    def fact(self, n):
        return self._fact[n]

    def invfact(self, n):
        return self._invfact[n]

    def comb(self, n, k):
        return self._fact[n] * self._invfact[k] % MOD * self._invfact[n - k] % MOD if 0 <= k <= n else 0

    def perm(self, n, k):
        return self._fact[n] * self._invfact[n - k] % MOD if 0 <= k <= n else 0

if __name__ == "__main__":
    mf = ModFact(100)
    print(mf.inv(3))
    print(mf.comb(10, 3))
    print(mf.perm(10, 3))