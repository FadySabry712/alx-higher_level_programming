#!/usr/bin/python3
def magic_calculation(a, b):
    result_of_cal = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result_of_cal += (a ** b) / i
        except Exception:
            result_of_cal = b + a
            break
    return result_of_cal
