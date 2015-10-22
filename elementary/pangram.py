# http://www.checkio.org/mission/pangram

import string
check_pangram = lambda s: sum([int(c not in s.lower()) for c in string.ascii_lowercase]) == 0

if __name__ == '__main__':
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
