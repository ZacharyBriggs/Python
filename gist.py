#user_string = input("Input a word.")
user_string = "fuxck"
num_vowels = 0
string_len = len(user_string)
for i in range(0,string_len):
    for uppcaser_iter in range(65,90):
        if int(user_string[i]) == uppercase_iter:
            print user_string[i]
    if i%2 > 0:
        print user_string[i]
    if int(user_string[i]) == 65 or int(user_string[i]) == 69 or int(user_string[i]) == 73 or int(user_string[i]) == 79 or int(user_string[i]) == 85 \
    or int(user_string[i]) == 97 or int(user_string[i]) == 101 or int(user_string[i]) == 105 or int(user_string[i]) == 111 or int(user_string[i]) == 117:
        user_string[i] = '_'
        num_vowels += 1
print user_string
print num_vowels