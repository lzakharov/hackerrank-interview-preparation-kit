INF = 1000000000


def main():
    n = int(input())
    is_cumulus = list(map(lambda x: x == '0', input().split()))

    dp = [0] * n
    dp[1] = 1 if is_cumulus[1] else INF

    for i in range(2, n):
        if is_cumulus[i]:
            dp[i] = min(dp[i - 1], dp[i - 2]) + 1
        else:
            dp[i] = INF

    print(dp[-1])


if __name__ == '__main__':
    main()
