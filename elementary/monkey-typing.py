# http://www.checkio.org/mission/monkey-typing

def count_words(text, words):
    return sum([1 for word in words if text.lower().find(word) >= 0])

if __name__ == '__main__':
    assert count_words(
        "How aresjfhdskfhskd you?",
        {"how", "are", "you", "hello"}
    ) == 3, "Example"
    assert count_words(
        "Bananas, give me bananas!!!",
        {"banana", "bananas"}
    ) == 2, "BANANAS!"
    assert count_words(
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
        {"sum", "hamlet", "infinity", "anything"}
    ) == 1, "Weird text"

