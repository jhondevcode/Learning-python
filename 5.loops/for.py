# for loop in python

for i in range(0, 10):
    print(i)

# pairs
for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print(number, ": Fizz buzz")
    elif number % 3 == 0:
        print(number, ": Fizz")
    elif number % 5 == 0:
        print(number, ": Buzz")
