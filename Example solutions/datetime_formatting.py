from datetime import datetime

# Open file and create Datetime timestamp
with open("loan_requests.txt", "w") as f :
    timestamp = datetime.now().strftime("%d %b %Y at %H:%M:%S")
    f.write(timestamp)