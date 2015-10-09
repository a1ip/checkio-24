# http://www.checkio.org/mission/boolean-algebra

def boolean(x, y, operation):
    if operation == 'conjunction':
        return int(x and y)
    elif operation == 'disjunction':
        return int(x or y)
    elif operation == 'implication':
        return int(not x or y)
    elif operation == 'exclusive':
        return int(not (x == y))
    return int(x == y)

if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
