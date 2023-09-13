string  = 'HelloMyString'

# task 00

print(string.lower())

# task 01

string2 = 'tutu on the tuki-kata'

print(string2.replace('tu','ta'))

# task 02

# The code search into a string the string 'a' and display the index of 'a' contains on the string

# task 03 

p = 'abdefghij' # output with (p[:: -2][:5][:: -1][3:]) => 1- jhfda 2- jhfda - adfhj - hj

print(p[:: -2][:5][:: -1][3:])

# task 04

q = 'abdefghij'

print(q[:: -2][:: -1][3:])

# task 05

for i in range(10):
    print(f'{i+1} : dixfois', end='\n')

# task 06

chaine = print('je suis affiché 10 fois\n'*10)

# task 07

s1 = "Hello"
s2 = 42
concat = s1 + str(s2)
print(concat)

# task 08

string1 = "42"
string2 = "is"
string3 = "the answer"
concat = string1 + ' ' + string2 + ' ' + string3
print(f'The string "{concat}" contains {len(concat)} characters.')