import random
true_chars = []
words = ["tree", "beach","clock","banana","book","android","python","sand"]
word = random.choice(words)
score = len(word)
for i in range(len(word)):
    print("-",end = " ")

while score != 0:
    char = input("\nPlease enter the character:")
    if char in word:
        true_chars.append(char)
        print(" it was true . your Score:",score)
    else:
        score = score - 1
        print("it was false . your Score:",score)

    if len(word) == len(true_chars):
        print("You won!, you guessed all the letters of {} truly.".format(word))
        break
    if score == 0:
        print("you lose! The word was {}".format(word))
        break