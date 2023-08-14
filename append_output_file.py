# Appending, writting output to the file.
import sys
from datetime import datetime

now = datetime.now()
message = f'{now:%M:%S} Logged!'
print(message) #prints minutes and second

out = open('out.text','a') # open output file, data need to be append.

with open('logs.text', 'a') as file:
    print(message, file=out)
    # the output(message) is appended to the file(out.text) or we can pass logs.text as file=file
