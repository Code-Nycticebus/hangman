from random import choice

def load_word_list() -> list[str]:
    word_list: list[str] = []
    with open("res/words.txt", "r") as f:
        for line in f.readlines():
            word_list.append(line.strip().lower())
    return word_list 


def game():
    word: str = choice(load_word_list())   
    guesses: list[str] = list("_" for _ in word)
    game_over: bool = False
    max_tries: int = 11

    while (not game_over):
        print(" ".join(guesses))
        i = input(f"{max_tries} tries left. Type you guess: ").lower()
        for letter in i:
            if letter in word:
                index = word.find(letter)
                while (index != -1):
                    guesses.pop(index)
                    guesses.insert(index, letter)
                    index = word.find(letter, index+1)
            else:
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

