def triangular(angka):
    total = 0
    data = range(1,angka + 1)
    it = iter(data)
    for i in it:
        total+=i
    return total

print(triangular(5))