n = 0

while n < 5:
    print("while loop: ", n)
    n += 1
# >>> 0 1 2 3 4

# Looping from 1 = 0 to 1 = 4
for  i in range(5):
    print("for i in range: ", i)
# >>>  0 1 2 3 4

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print("i: ", i)
# First value is starting value and the second one is end value

# Looping for i = 5 to i = 2
for i in range(5, 1, -1):
    print("dec i: ", i)
# First value is starting value and the second one is end value and the last value is decrement or increment value