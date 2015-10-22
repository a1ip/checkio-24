# http://www.checkio.org/mission/number-radix

def checkio(n, r):
    res = []
    for i,c in enumerate(n[::-1]):
        t = int(c) if c.isdigit() else 10 + (ord(c) - ord('A'))
        if t >= r:
            return -1
        res += [(r ** i) * t]
    return sum(res)

if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
