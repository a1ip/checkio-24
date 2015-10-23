# http://www.checkio.org/mission/common-words


checkio = lambda x,y: ','.join(sorted([w for w in x.split(',') if w in y.split(',')]))


if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
