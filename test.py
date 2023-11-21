# Silly little script for making joke posts on Discord made in like 5 minutes
string = input("Enter a string:")

splt_string = string.split(" ")

longest_word = len(max(splt_string, key=len))
number_of_words = len(splt_string)
output = [[" "] * number_of_words for _ in range(longest_word)]


for word_number, word in enumerate(splt_string):
    for letter_number, letter in enumerate(word):
        column_number = word_number - number_of_words
        output[letter_number][-(word_number + 1)] = letter

print("```")
for row in output:
    print(" ".join(row))
print("```")
