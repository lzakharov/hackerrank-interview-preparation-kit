def main():
    n, m = map(int, input().split())
    xs = [0] * (n + 2)

    for _ in range(m):
        a, b, k = map(int, input().split())
        xs[a] += k
        xs[b + 1] -= k

    answer = 0
    current = 0

    for x in xs:
        current += x
        answer = max(answer, current)

    print(answer)


if __name__ == '__main__':
    main()
