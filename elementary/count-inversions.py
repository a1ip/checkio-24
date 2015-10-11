# http://www.checkio.org/mission/count-inversions


def count_inversion(x):
    return sum(
        1 for i in range(len(x))for j in range(i+1, len(x)) if x[i] > x[j]
    )

if __name__ == '__main__':
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
