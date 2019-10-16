word = input()

# Remove the newline \n character read from the input
word = word.strip()

uppercase = 0
lowercase = 0

for character in word:
    if character.isupper():
        uppercase += 1
    else:
        lowercase += 1

if uppercase > lowercase:
    word = word.upper()
else:
    word = word.lower()

print(word)