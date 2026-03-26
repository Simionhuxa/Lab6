import urllib.parse
import pyperclip

url = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"

decoded_url = urllib.parse.unquote(url)

print("Закодоване посилання:")
print(url)

print("\nДекодоване посилання:")
print(decoded_url)

pyperclip.copy(decoded_url)
print("\nПосилання скопійовано в буфер обміну.")