# Test if an int > 2 is prime.
# If not then print smallest divisor.
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2,x):
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')


# Below is the same program, but significantly faster,
# reducing numbers checked by half
smallest_divisor = None
if x % 2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x % guess == 0:
            smallest_divisor = guess
            break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')