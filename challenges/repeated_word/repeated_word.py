def repeated_word(string):
    hash_table = {}
    words = string.split(' ')
    for word in words:
        if word not in hash_table:
            hash_table[word] = 1
        else:
            return word


