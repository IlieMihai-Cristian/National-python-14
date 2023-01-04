# cuvant = 't e m p e r a m e n t'
        # t _ _ _ _ _ _ _ _ _ t
# reguli:
# - daca litera inceput sau litera sfarsit se mai gaseste in interior, aceasta se va afisa;
# - 6 incercari;

word = "temperament"
start_letter = word[0]
end_letter = word[-1]
display_word = word
for i in display_word:
    if i == start_letter or i == end_letter:
        continue
    else:
        display_word = display_word.replace(i, '_')
    # if i != start_letter and i != end_letter:
    #     i = '_'
    # display_word += i
attempts = 6
tried_char = []
while attempts > 0:
    print(f"Cuvantul este: {display_word}. Mai aveti {attempts} incercari")
    letter = input("Introduceti litera: ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print('Va rugam introduceti doar o litera!')
        continue
    if letter in [start_letter, end_letter] and letter not in tried_char:
        tried_char.append(letter)
    if letter in tried_char:
        print(f'Ai mai incercat litera {letter}. Ati incercat pana acum literele {tried_char}')
    else:
        tried_char.append(letter)
        if letter in word.lower():
            for i in range(len(word)):
                if word[i] == letter:
                    display_word = display_word[:i] + word[i] + display_word[i+1:]
            if '_' not in display_word:  # if word.lower() == display_word.lower()
                print(f"Felicitari! Ati castigat! Cuvantul gasit este '{word}'")
                break
        else:
            attempts -= 1
            print(f'Litera {letter} nu se afla in cuvant!')
            if attempts == 0:
                print(f'Ati pierdut. Cuvantul cautat era {word}')

