old_list = [11, 3, 7, 0, 5, 2, -10, 8, 9, 10]
new_list = []
value = input("Pick a number.\n")
for i in range (0,len(old_list)):
    if old_list[i] < value:
        new_list.append(old_list[i])        
print new_list