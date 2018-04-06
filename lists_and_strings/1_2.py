#!/usr/bin/env python3

# Task description
# Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
# five characters, including the null character.)

def reverse(word):
    reversed = ""
    # Loop through each letter of the string passed in to the function from back-to-front
    # and append each letter in to the above variable, excluding the null string at the end.
    for letter in range(len(word)-1, -1, -1):
        reversed = reversed + word[letter]
    # Now append the null string
    reversed = reversed + word[len(word)-1]

    print(reversed)


if __name__ == '__main__':
    reverse('Pool\0')
    reverse('Police\0')
    reverse('Monitor\0')
