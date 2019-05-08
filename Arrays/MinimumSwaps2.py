def main():
    n = int(input())
    a = list(map(int, input().split()))
    answer = 0
    used = [False] * n

    for i in range(n):
        if not used[i]:
            used[i] = True
            j = a[i] - 1
            while j != i:
                used[j] = True
                answer += 1
                j = a[j] - 1

    print(answer)


if __name__ == '__main__':
    main()
