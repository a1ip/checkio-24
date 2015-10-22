# http://www.checkio.org/mission/days-diff/solve/

from datetime import datetime as dt


days_diff = lambda d1, d2: abs(
    (dt(d1[0], d1[1], d1[2]) - dt(d2[0], d2[1], d2[2])).days
)


if __name__ == '__main__':
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
