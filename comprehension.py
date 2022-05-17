import random


random_list = []

[random_list.append(random.randint(0, 100)) for i in range(10)]

squared = [x ** 3 for x in random_list if x % 3 == 0]
print(squared)