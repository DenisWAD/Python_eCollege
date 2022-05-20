my_list = ["life", "answer", 42, 0]

for thing in my_list:
    if thing == 0:
        my_list[thing] = "universe"
    elif thing == 42:
        my_list[1] = "everything"

print(my_list)