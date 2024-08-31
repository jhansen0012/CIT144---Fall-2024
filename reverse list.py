def main():
    word_user = user_word[::-1]
    print(word_user)

user_word = []

user_ini = input(str("Think of a word, type it here. I'll type it back to you letter by letter in reverse!"))
for letter in user_ini:
    user_word.append(letter)

main()