#1. Design a function that reverses the digit of an integer. for, example , 50 should be 5 and -12 be -21
user_input = int(input("Input an integer: ")) #User inputs integer
def reverse_digits(num):
    is_negative = num < 0
    num = abs(num)
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if is_negative:
        reversed_num = -reversed_num

    return reversed_num
result = reverse_digits(user_input)

print("Reversed integer is:", result)


#2. Write a recursive function to culculate the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
user_input = int(input("Enter a number to calculate its factorial: "))
result = factorial(user_input)
print(f"The factorial of {user_input} is: {result}")    



#3. Design a function that takes a string or a sequence of characters as input and returns the characters  that appears most frequently.
def most_frequent_char(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_frequent = max(char_count, key=char_count.get)
    return most_frequent

user_input = input("Enter a string: ")

result = most_frequent_char(user_input)
print(f"The most frequent character in '{user_input}' is: {result}")


#4. Design a function that determines whether a given string is a pangram.
def is_pangram(string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    lowercase_string = string.lower().replace(' ', '')
    return set(lowercase_string) >= alphabet


user_input = input("Enter a string to check if it's a pangram: ")


if is_pangram(user_input):
    print(f"The string '{user_input}' is a pangram.")
else:
    print(f"The string '{user_input}' is not a pangram.")


#5. Design a function that takes a list of integers as input. The function should return True if the list containss two consequetive integers anywhere within the list, otherwise return False
def has_consecutive_threes(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False


user_input = input("Enter a list of numbers: ")
numbers = [int(num) for num in user_input.split()]


if has_consecutive_threes(numbers):
    print("The list contains two consecutive threes.")
else:
    print("The list does not contain two consecutive threes.")


#6. Design a function that takes input as sentences and returns a new sentence with a words reversed as in the same order Master  Yoda would use.
def yoda_speak(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    yoda_sentence = ' '.join(reversed_words)
    return yoda_sentence


user_input = input("Enter a sentence: ")



yoda_version = yoda_speak(user_input)
print(f"Yoda-style version: {yoda_version}")
