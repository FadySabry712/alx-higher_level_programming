#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argString = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argString += 's.'
elif argc == 1:
    argString += ':'
else:
    argString += 's:'
print(argString.format(argc))

j = 0
for arg in sys.argv:
    if j != 0:
        print("{:d}: {:s}".format(i, arg))
    j += 1
