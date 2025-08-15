# Develop a program that takes a user-entered sentence and performs operations like string concatenation, slicing, and checks for the presence of a specific word.

sentence = input("Enter a sentence: ")

new_sentence = sentence + " - This is a Python program."
print("After concatenation:", new_sentence)

slice_part = sentence[:5]
print("First 10 characters:", slice_part)

word_to_check = input("Enter a word to check: ")
if word_to_check in sentence:
    print(f"The word '{word_to_check}' is present in the sentence.")
else:
    print(f"The word '{word_to_check}' is not present in the sentence.")
