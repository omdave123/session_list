#Program for vowels v/s consonants

print("------- continue statements -------")
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        continue
    print("the letters are:", letter)

print("------- Break statments-------")
for letter in 'zyxwvutsrqponmlkjihgfedcba':
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        break
    print("The letters are:", letter)
