# http://www.checkio.org/mission/digits-multiplication

checkio = lambda x:eval('*'.join([n for n in str(x) if n != '0']))

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
