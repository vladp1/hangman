import random

English_lowercase_letters =  {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'} 

print("H A N G M A N")
answer_words = ('python', 'java', 'kotlin', 'javascript')
random.seed()

while True:
    answer = input('Type "play" to play the game, "exit" to quit:')
    if answer == "exit":
        break
    elif answer == "play":
        answer_word = random.choice(answer_words)
        letters = set()
        output_str = ""

        lives = 8
        while lives:
            print()
            output_str = ""
            for i in answer_word:
                output_str += i if i in letters else "-"
            print(output_str)
            if output_str == answer_word:
                print("You guessed the word!")
                break

            letter = input("Input a letter: ")
            if not (len(letter) == 1):
                print("You should input a single letter")
            elif letter not in English_lowercase_letters:
                print("Please enter a lowercase English letter")
            elif letter in letters:
                print("You've already guessed this letter")
            else:     
                letters.add(letter)
                if letter not in answer_word:
                    print("That letter doesn't appear in the word")
                    lives -= 1
    
        if output_str == answer_word:
            print("You survived!")
        else:
            print("You lost!")
        print()
print("Thanks for playing!")
