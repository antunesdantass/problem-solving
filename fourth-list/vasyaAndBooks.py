value = raw_input()
actual = value
sum = 0
while actual != "0":
    biggest = int("9" * (len(actual) - 1)) if len(actual) > 1 else 0
    actualInt = int(actual)
    sum += (actualInt - biggest) * len(actual)
    actual = str(biggest)

print sum