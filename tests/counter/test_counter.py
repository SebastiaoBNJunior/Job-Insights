from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    word = 'Python'

    result = count_ocurrences(path, word)
    expected = 1639

    assert result == expected, 'Contagem correta para a palavra "Python"'
