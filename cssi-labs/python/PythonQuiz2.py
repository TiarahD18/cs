Exercise 1
def SmallestNumber(x, y, z):
    least = x;
    if y < least:
        least = y
    if z < least:
        least = z
    return least

#Exercise 2
def SumOfEven(n):
    sum = 0
    for i in range(n):
        sum = sum + 2 + (i + 1)
        return sum
