#!/usr/bin/env python3

# Task description
# Implement an algorithm to determine if a string has all unique characters. What if you
# can not use additional data structures?

def check_unique(word):
    buffer = ""
    # Iterate through the string passed in to the function
    for letter in word:
        # Check if the letter exists in the buffer string.
        # If it exists, then break out from the loop as the string is not unique.
        if letter in buffer:
            print("The string does not contain all unique characters.")
            break
        else:
            # We've encountered the first occurrence of letter, so append it in to
            # the buffer for comparison in the next iteration of the loop
            buffer = buffer + letter

    if buffer == word:
        print("The string contains all unique letters.")


if __name__ == "__main__":
    check_unique("Pool")
    check_unique("Police")
    check_unique("Endeavor")
    check_unique("AWS")
    check_unique("Google")
    check_unique("ghwuaighiaewhgjkwea")
