# http://www.checkio.org/mission/fizz-buzz/

def checkio(number):
    res = []
    if number % 3 == 0:
        res.append('Fizz')
    if number % 5 == 0:
        res.append('Buzz')
    return ' '.join(res) or str(number)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
