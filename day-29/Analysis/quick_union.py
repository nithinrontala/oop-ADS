class QuickUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        self.parent[rootP] = rootQ
        self.count -= 1
