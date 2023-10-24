# import modules
import string
import random


# store all characters in lists
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
punctuations = list(string.punctuation)

# Ask user about the number of characters
pass_lenght = input("How long should be your password? ")

# check this input is it number? is it more than 8?
while True:
    try:
        characters_number = int(pass_lenght)
        if characters_number < 8:
            print("Your number should be at least 8.")
            pass_lenght = input("Please, enter your number again: ")
        else:
            break
    except:
        print("Please, enter numbers only.")
        pass_lenght = input("How long should be your password? ")

# shuffle all lists
random.shuffle(lowercase)
random.shuffle(uppercase)
random.shuffle(digits)
random.shuffle(punctuations)

# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30 / 100))
part2 = round(characters_number * (20 / 100))

# generation of the password (60% letters and 40% digits & punctuations)
result = []

for i in range(part1):
    result.append(lowercase[i])
    result.append(uppercase[i])

for i in range(part2):
    result.append(digits[i])
    result.append(punctuations[i])

# shuffle result
random.shuffle(result)

# join result
password = "".join(result)
print("Your Password: ", password)
