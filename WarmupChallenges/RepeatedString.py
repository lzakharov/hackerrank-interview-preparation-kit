def main():
    s = input()
    n = int(input())

    count = s.count('a')
    answer = (n // len(s)) * count
    answer += s[:n % len(s)].count('a')

    print(answer)


if __name__ == '__main__':
    main()
