# task 00

name = input("What's your name : ")

print(f"Hello {name}")

# task 01

name = input("What's your name capitalize (first letter) : ")

final_name = name[0].capitalize() + name[1:]

print(f"Hello {final_name}")

# task 02

first_number = int(input("First number : "))
second_numver = int(input("Second number : "))

res = first_number + second_numver

print(f"The sum is : {res}")

# task 03

number = int(input("Number : "))

print(type(number)) # Affiche le type de la variable number

# task 04

string_to_extract = 'This is a test. Is it possible to fly? Good things come to those who never give up. But okay'

sentences = string_to_extract.split('.') + string_to_extract.split('?')

sentences.sort(reverse=True)

first_words = []

for sentence in sentences:
    words = sentence.strip().split(' ')
    if words[0] and words[0] not in first_words:
        first_words.append(words[0])

final = ' '.join(first_words)

print(final)

