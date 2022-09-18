def remove_ends_with_vowel(words_list):
    vowels = "aeiou"
    wl = words_list[:]
    for word in wl:
        if word[-1] in vowels:
            words_list.remove(word)
    return words_list


words = ["answer", "anna", "soda", "uncle", "acknowledge"]
remove_ends_with_vowel(words)
print(words)
words = ["hello", "goodbye", "yes", "no", "why"]
remove_ends_with_vowel(words)
print(words)
