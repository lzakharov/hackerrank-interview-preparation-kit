INF = 101


def main():
    a = [list(map(int, input().split())) for _ in range(6)]
    answer = -INF

    for i in range(1, 5):
        for j in range(1, 5):
            total = (sum(a[i - 1][j - 1: j + 2]) +
                     a[i][j] + sum(a[i + 1][j - 1: j + 2]))
            answer = max(answer, total)

    print(answer)


if __name__ == '__main__':
    main()
