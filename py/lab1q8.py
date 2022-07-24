vowel_list = []

input_file = open("/Users/nan/Projects/fsd/max/test1.txt", "r")
text = input_file.read().split()
input_file.close()

for word in text:
    if word[0] in "AEIOUaeiou":
        vowel_list.append(word)

max_len = len(max(vowel_list, key = len))
longest_vowel = [word for word in vowel_list if len(word) == max_len]
print('The longest word is "', longest_vowel, '"', sep="")