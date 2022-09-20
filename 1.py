def sum_squares(*args):
    sum = 0
    for i in args:
        sum+=i**2
    return sum

print(sum_squares(1,2,3))