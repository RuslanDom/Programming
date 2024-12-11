from lorem_text import lorem


def main():
    with open('../Asyncio/chapter_6/random_words.txt', 'w') as file:
        words = lorem.words(10000000).split()
        for w in words:
            file.write(w + '\n')

    with open('../Asyncio/chapter_6/random_words.txt', 'r') as file_read:
        res = [word.strip('\n') for word in file_read.readlines()]
        print(res)


if __name__ == "__main__":
    main()
