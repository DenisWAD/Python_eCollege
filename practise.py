def get_first_capital(some_string) :
    capital = None

    for i in some_string :
        if i.upper() == i and i != " " :
            capital = i
            break

    if capital == None :
        return "No capital was found"
    else :
        return "Capital letter found. It is: " + capital


first_capital = get_first_capital("denis murrAy")

print(first_capital)