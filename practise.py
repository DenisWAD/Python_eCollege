import random


random_list = []

# for i in range(10) :
#   random_list.append(random.randint(0, 100))

[random_list.append(random.randint(0, 100)) for j in range(10) ]

for i in random_list :
  if i % 7 == 0 :
    continue
  elif i == 315 :
    break

  print(i)

# print(random_list)