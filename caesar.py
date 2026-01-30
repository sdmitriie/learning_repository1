test_variable = 8

rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"


def replace_letters(words, alpha_lower):
    string = "".join([letter for letter in words if letter.isalpha() or letter == " "])
    string = string.split()
    list_with_lenght = [len(word) for word in string]
    if list_with_lenght == []:
        return words

    new_words = ""
    alpha_upper = alpha_lower.upper()
    x = 0
    for letter_in_word in words:

        caesar_key = list_with_lenght[x]
        if not letter_in_word.isalpha() and letter_in_word != " ":
            new_words += letter_in_word
        elif letter_in_word == " ":
            new_words += letter_in_word
            if x == len(list_with_lenght) - 1:
                continue
            else:
                x += 1

        elif letter_in_word.isupper():
            for letter_in_alphabet in alpha_upper:
                if letter_in_word == letter_in_alphabet:
                    if (alpha_upper.index(letter_in_alphabet) + caesar_key + 1) <= len(
                        alpha_upper
                    ):
                        new_words += alpha_upper[
                            alpha_upper.index(letter_in_alphabet) + caesar_key
                        ]
                        break

                    else:
                        new_words += alpha_upper[
                            alpha_upper.index(letter_in_alphabet)
                            - len(alpha_upper)
                            + caesar_key
                        ]
                        break
        elif letter_in_word.islower():
            for letter_in_alphabet in alpha_lower:
                if letter_in_word == letter_in_alphabet:
                    if (alpha_lower.index(letter_in_alphabet) + caesar_key + 1) <= len(
                        alpha_lower
                    ):
                        new_words += alpha_lower[
                            alpha_lower.index(letter_in_alphabet) + caesar_key
                        ]
                        break

                    else:
                        new_words += alpha_lower[
                            alpha_lower.index(letter_in_alphabet)
                            - len(alpha_lower)
                            + caesar_key
                        ]
                        break
    return new_words


words = input()


new_words = replace_letters(words, alpha_lower)
print(new_words)
