#pylint: disable=W0614
from random import *
def main():
    words = open("words.txt", 'r')
    rand = randint(0, 76)
    num = 0
    for word in words:
        if rand is num:
            print word
        num += 1
    words.close()
main()