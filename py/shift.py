def shifting(words, index):
    words.remove(words[index])
    i = len(words) - index
    words.insert(i,words[i])

words1 = ["mia", "sofia", "harper", "elle", "benjamin"]
words2 = ["cake", "apple", "orange", "pumpking", "egg"]
shifting(words1, 3)
print(words1)
shifting(words2, 4)
print(words2)