#All 3 Problem Solving Challenges
#Reverse a String
# Input string
text = "hello"

# Reverse using slicing
reversed_text = text[::-1]

print("Reversed String:", reversed_text)  # Output: Reversed String: olleh

#Count Vowels in a String
# Input string
text = "I love Python programming!"

# Define vowels
vowels = "aeiouAEIOU"

# Counter
count = 0

# Loop through each character
for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)  # Output: Number of vowels: 7


#Sum of Digits of a Number
# Input number
number = 1234

# Convert number to string to loop over digits
number_str = str(number)

# Initialize sum
total = 0

# Loop through each digit
for digit in number_str:
    total += int(digit)

print("Sum of digits:", total)  # Output: Sum of digits: 10
