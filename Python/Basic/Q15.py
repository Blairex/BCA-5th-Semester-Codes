# Write a program to take input for a sentence and sort the words according to their length.

sentence = input("Enter a sentence: ")
words = sentence.split()
sorted_words = sorted(words, key=len)
print("Words sorted by length:", sorted_words)
