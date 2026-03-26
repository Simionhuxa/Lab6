import re

# український алфавіт
ukrainian_letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def word_key(word):
    first_letter = word[0].lower()

    if first_letter in ukrainian_letters:
        return (0, word.lower())   # спочатку українські
    elif first_letter.isalpha():
        return (1, word.lower())   # потім латинські
    else:
        return (2, word.lower())   # потім все інше

# читаємо файл
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Початковий текст:\n")
print(text)

# беремо слова без розділових знаків
words = re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE)

sorted_words = sorted(words, key=word_key)

print("\nВідсортовані слова:\n")
for word in sorted_words:
    print(word)