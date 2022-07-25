"""Convert command line arguments into list of int"""
import sys

requests = []

for x in sys.argv[1:] :
    requests.append(int(x))
