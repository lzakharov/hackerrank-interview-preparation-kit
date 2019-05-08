def main():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    d %= n
    answer = a[d:] + a[:d]

    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()
