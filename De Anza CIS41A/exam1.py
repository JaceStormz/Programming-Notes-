def countMatches(secret, guess):
    matches = 0
    for i in range(len(secret)):
        if i < len(guess) and secret[i] == guess[i]:
            matches += 1
    return matches


def main():
    mysteryWord = "lazy"  # Hardcoded value
    mysteryWord = mysteryWord.lower()

    print(f"The mystery word has {len(mysteryWord)} letters.")

    while True:
        guess = input("Enter your guess: ").lower()

        if guess == mysteryWord:
            print("Correct, You guessed the word.")
            break

        correctLetters = countMatches(mysteryWord, guess)
        print(f"{correctLetters} letter(s) are correct and in the correct position.")


main()