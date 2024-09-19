#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for argument in sys.argv:
        if argument != sys.argv[0]:
            result += int(argument)
    print(result)
