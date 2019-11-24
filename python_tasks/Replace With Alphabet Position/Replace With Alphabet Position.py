from string import ascii_lowercase

#LETTERS = {key: str(value) for value, key in enumerate(ascii_lowercase, start=1)}
LETTERS = {}

for key, value in enumerate(ascii_lowercase, start=1):
    LETTERS[value] = str(key)

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers) 