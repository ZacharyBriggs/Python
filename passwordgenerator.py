#pylint: disable=W0614
#pylint: disable=E1601
from random import *
def main():
    words = open("words.txt", 'r')
    password = open("passwords.txt", 'a')
    rand = randint(1, 76)
    rand_two = randint(1,76)
    iterator = 0
    strength = 0
    strength = input("Choose your password strength. 0-5\n")
    #Outputs a random word
    if strength is 0:
        for rand_word in words:
            iterator += 1
            if rand is iterator:
                print rand_word
                password.write(rand_word)
    #Outputs a random word + a random letter
    elif strength is 1:
        for rand_word in words:
            iterator += 1
            if rand is iterator:
                rand_num = randint(0, 100)
                rand_word += str(rand_num)
                password.write(rand_word)
                password.write("\n")
                print rand_word
    #Outputs a random word + a random number + a special character
    elif strength is 2:
        for rand_word in words:
            iterator += 1
            if rand is iterator:
                rand_num = randint(0,100)
                rand_word += str(rand_num)
                password.write(rand_word)
                password.write("\n")
    #Outputs 2 randomwords + a random number + a special character + first letter is uppercased
    elif strength is 3:
        for rand_word in words:
            iterator += 1
            if rand is iterator:
                iterator = 0
                for rand_word_two in words:
                    iterator += 1
                    if rand_two is iterator:
                        if int(rand_word[0]) > 96:
                            rand_word[0] -= 32
                        rand_num = randint(0,100)
                        rand_word += rand_word_two
                        rand_word += str(rand_num)
                        print rand_word
                        password.write(rand_word)
                        password.write("\n")
    #Outputs 2 randomwords + a random number + a special character + all convertable letters are changed into a special character
    elif strength is 4:
        for rand_word in words:
            iterator += 1
            if rand is iterator:
                iterator = 0
                for rand_word_two in words:
                    iterator += 1
                    if rand_two is iterator:
                        if int(rand_word[0]) > 96:
                            rand_word[0] -= 32
                        rand_num = randint(0,100)
                        rand_word += rand_word_two
                        rand_word += str(rand_num)
                        print rand_word
                        password.write(rand_word)
                        password.write("\n")
    #Outputs 2 random words + a random number + a special character + all convertable letters are changed into a special character + all convertable letters are changed into a number
    elif strength is 5:
        print "none"
    else:
        print "Invalid Input"
    words.close()
main()