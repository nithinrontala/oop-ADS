class QuickFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.count = n  # number of components

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return

        # Rename all p_id entries to q_id
        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id
        self.count -= 1
