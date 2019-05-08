from collections import Counter


def main():
    _ = input()
    colors = list(map(int, input().split()))

    answer = sum(map(lambda x: x // 2, Counter(colors).values()))

    print(answer)


if __name__ == '__main__':
    main()
