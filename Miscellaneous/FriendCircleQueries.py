def root(parent, a):
    while a != parent[a]:
        a = parent[a]
    return a


def main():
    queries = int(input())

    parent = {}
    size = {}
    answer = [1] * queries
    max_size = 1

    for query in range(queries):
        a, b = map(int, input().split())
        parent[a] = parent.get(a, a)
        parent[b] = parent.get(b, b)
        size[a] = size.get(a, 1)
        size[b] = size.get(b, 1)

        pa = root(parent, a)
        pb = root(parent, b)

        if pa != pb:
            if size[pa] > size[pb]:
                parent[pb] = pa
                size[pa] += size[pb]
            else:
                parent[pa] = pb
                size[pb] += size[pa]

        max_size = max(max_size, max(size[pa], size[pb]))

        answer[query] = max_size

    print(*answer, sep='\n')


if __name__ == '__main__':
    main()
