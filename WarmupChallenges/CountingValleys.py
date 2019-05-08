def main():
    _ = input()
    path = input()

    level = 0
    answer = 0

    for step in path:
        if step == 'U' and level == -1:
            answer += 1
        level += 1 if step == 'U' else -1

    print(answer)


if __name__ == '__main__':
    main()
