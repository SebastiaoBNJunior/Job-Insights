def count_word_ocurrences(path, word):
    file = open(path, encoding="utf-8")
    read_data = file.read()
    word_count = read_data.count(word)
    return word_count
