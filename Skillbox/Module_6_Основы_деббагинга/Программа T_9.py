from typing import List

LETTERS_DATA = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}

def get_words():
    with open("/usr/share/dict/words") as file:
        return [word.strip('\n') for word in file.readlines()]


def my_t9(input_numbers: str) -> List[str]:
    middle = []
    letters = [LETTERS_DATA[int(num)] for num in input_numbers]
    words = get_words()  # Список всех слов
    for l in range(len(letters)):
        for word in words:
            if len(word) == len(letters):
                if l == 0 and word[l] in letters[l]:
                    middle.append(word)
                elif word[l] in letters[l]:
                    continue
                else:
                    if word in middle:
                        middle.remove(word)
    return middle




if __name__ == '__main__':
    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')