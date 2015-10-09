# http://www.checkio.org/mission/three-words

import re
checkio = lambda x:True if re.search('\D+\s\D+\s\D+', x) else False

if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

