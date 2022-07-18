import sys

old = sys.stdout

sys.stdout = open("txtfile.txt", "w")

print("This is output to a new text file")
