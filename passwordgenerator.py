#pylint: disable=W0614
from random import *
def main():
    words = open("words.txt", 'r')
    password = open("passwords.txt", 'a')
    rand = randint(1, 76)
    num = 0
    strength = 0
    strength = input("Choose your password strength. 0-5\n")
    if strength is 0:
        for word in words:
            num += 1
            if rand is num:
                print word
                password.write(word)
    elif strength is 1:
        for word in words:
            num += 1
            if rand is num:
                rand_num = randint(0, 100)
                word += str(rand_num)
                password.write(word)
                print word
    elif strength is 2:
        print "none"
    elif strength is 3:
        print "none"
    elif strength is 4:
        print "none"
    elif strength is 5:
        print "none"
    else:
        print "Invalid Input\n"
    words.close()
main()