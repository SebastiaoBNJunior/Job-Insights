def count_ocurrences(path: str, word: str) -> int:
    file = open(path, encoding='utf-8')
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    return word_count
