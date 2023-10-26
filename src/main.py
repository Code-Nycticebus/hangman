from random import choice

WORD_TEXT_FILE = "res/words_DE.txt"

def load_word_list() -> list[str]:
    word_list: list[str] = []
    with open(WORD_TEXT_FILE, "r") as f:
        for line in f.readlines():
            word_list.append(line.strip().upper())
    return word_list 


def game():
    word: str = choice(load_word_list())   
    guesses: list[str] = list("_" for _ in word)
    wrong_guesses: list[str] = []
    max_tries: int = 11

    game_over: bool = False
    while (not game_over):
        if len(wrong_guesses):
            print(f"Wrong guesses: {' '.join(wrong_guesses)}")
        print(" ".join(guesses))
        i = input(f"{max_tries} tries left. Type your guess: ").upper()
        print()
        for letter in i:
            if letter in word:
                index: int = -1
                while ((index := word.find(letter, index+1)) != -1):
                    guesses.pop(index)
                    guesses.insert(index, letter)
            else:
                wrong_guesses.append(letter)
                max_tries -= 1
                if max_tries == 0:
                    print("You lose")
                    print(f"Solution: {word}")
                    game_over = True
                    continue

        guessed_word = "".join(guesses)
        if guessed_word == word:
            print("You won!")
            print(f"Solution: {word}")
            game_over = True
            continue

if __name__ == "__main__":
    game()

