#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argStr = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argStr += 's.'
elif argc == 1:
    argStr += ':'
else:
    argStr += 's:'
print(argStr.format(argc))

j = 0
for arg in sys.argv:
    if j != 0:
        print("{:d}: {:s}".format(j, arg))
    j += 1
