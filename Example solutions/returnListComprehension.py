def generate_list_from_length(name, length) :
    return [name for i in range(length) ]


list_to_make = generate_list_from_length("Denis", 10)

print(list_to_make)