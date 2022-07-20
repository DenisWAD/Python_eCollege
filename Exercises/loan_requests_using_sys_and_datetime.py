"""This app allows the requesting of loans via command line arguments"""

import sys
from datetime import datetime
from time import strftime

# Define the kitty.
kitty = 500

# Define a list to hold the loan requests.
requests = []

# Code to read in command line arguments goes here.......
for x in sys.argv[1:] :
    requests.append(int(x))


# Open file and create Datetime timestamp
with open("loan_requests.txt", "w") as f :
    timestamp = datetime.now().strftime("%d %b %Y at %H:%M:%S")
    f.write(timestamp)

# Loop through the list of loan requests.
for request in requests:
    if request <= kitty:

        with open('loan_requests.txt', 'a') as file:
            file.write('\nRequest of ' + str(request) + ' paid in full.')

        print(str(request) + ' - Paid!')
        kitty -= request

    elif kitty > 0:
        print(request, 'request cannot be processed in full (Insufficient funds available). Amount paid: ', kitty)

        with open('loan_requests.txt', 'a') as file:
            file.write('\nRequest of ' + str(request) + ' could not be paid in full.Partial payment of ' + str(
                kitty) + ' made.')

        kitty -= kitty
    else:
        print('Request of ' + str(request) + ' is UNPAID!')

        with open('loan_requests.txt', 'a') as file:
            file.write('\nOutstanding Request:' + str(request))
