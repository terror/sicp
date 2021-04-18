# code is data!
from enum import Enum


class Message(Enum):
    FIRST = 1
    SECOND = 2


def main():
    pair = cons(2, 3)
    print(pair(Message.FIRST))
    print(pair(Message.SECOND))


def cons(x, y):
    def dispatch(message):
        return x if message == Message.FIRST else y
    return dispatch


if __name__ == '__main__':
    main()
