# http://www.checkio.org/mission/end-of-other/


def checkio(words_set):
    word_list = sorted(list(words_set), key=len)
    return any([word_list[i] in word_list[j][-len(word_list[i]):]
                for i in range(len(word_list))
                for j in range(i + 1, len(word_list))])

if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) is True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) is False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) is True, "duck to walk"
    assert checkio({"one"}) is False, "Only One"
    assert checkio({"helicopter", "li", "he"}) is False, "Only end"
