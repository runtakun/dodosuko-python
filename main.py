import random

words = {
    0: 'ドド',
    1: 'スコ',
}


def main():
    histories = []
    while True:
        d = random.choice([0, 1])
        print(words[d])
        histories.append(d)

        if histories[-12:] == [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ]:
            print("ラブ注入❤️")
            break


if __name__ == '__main__':
    main()
