# Variables are dynamically types
n = 0
print("n= ", n)

n = "abc"
print("n= ", n)

# Multiple assignments
n, m = 0.125, "abc"
print("n ",n, " m ", m)
n, m, z = 0.125, "abc", False
print("n ",n, " m ", m, " z ", z)

# Increment
n = n + 1 #good
n += 1 #good
#n++ #bad

# None is null (absence of value)
n = 4
n = None
print("n= ", n)