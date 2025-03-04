import time
from quick_find import QuickFind
from quick_union import QuickUnion
from weighted_quick_union import WeightedQuickUnion
from weighted_quick_union_path_compression import WeightedQuickUnionPathCompression

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # First line might contain n (the number of elements)
    # Then subsequent lines contain pairs
    pairs = []
    start_line = 1
    n = int(lines[0].strip())  # if the first line is the number of objects
    for line in lines[start_line:]:
        if line.strip():
            p, q = map(int, line.split())
            pairs.append((p, q))
    return n, pairs

def benchmark_union_find(UFClass, n, pairs):
    uf = UFClass(n)
    start = time.time()
    for p, q in pairs:
        if not uf.connected(p, q):
            uf.union(p, q)
    end = time.time()
    return end - start, uf.count

def main():
    input_files = ["tinyUF.txt", "mediumUF.txt", "largeUF.txt"]
    uf_classes = [QuickFind, QuickUnion, WeightedQuickUnion, WeightedQuickUnionPathCompression]
    uf_names = ["QuickFind", "QuickUnion", "WeightedQuickUnion", "WeightedQuickUnionPC"]

    for file_path in input_files:
        print(f"\n=== Running on {file_path} ===")
        n, pairs = read_input(file_path)

        for UFClass, name in zip(uf_classes, uf_names):
            elapsed_time, component_count = benchmark_union_find(UFClass, n, pairs)
            print(f"{name} took {elapsed_time:.4f} seconds. Components left: {component_count}")

if __name__ == "__main__":
    main()
