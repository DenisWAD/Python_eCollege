requests = [] 
fileline = ""
kitty = 500

# Take info from .txt file
with open("C:\\Users\\denis\\Desktop\\Python\\Course submissions\\Assessment 2\\loan_requests.txt", "r") as file :
    for i in file :
        # Remove trailing new line using strip()
        fileline = i.strip()
        # Input data from file in existing list
        requests.append(int(fileline))

with open("C:\\Users\\denis\\Desktop\\Python\\Course submissions\\Assessment 2\\loan_requests.txt", "a") as file :
    # Check if loan requests can be paid
    for i in requests :
        if kitty <= 0 :
            print(f"Request of {i} is UNPAID!")
            file.write(f"\nOutstanding Request: {i}")
        elif (i > kitty) and kitty > 0 :
            print(f"{i} cannot be processed in full (Insufficient funds available). Amount paid: {kitty}")
            file.write(f"\nRequest of {i} could not be paid in full. Partial payment of {kitty} made.")
            kitty -= i
        else:
            print(f"{i} - Paid!")
            file.write(f"\nRequest of {i} paid in full.")
            kitty -= i


