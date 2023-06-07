# Strings are almost similar to arrays
s = "abc"
print(s[0:2]) #ab

# But strings are not mutable
#s[0] = "A" #this will not work

# This craates a new string
s += "def"
print(s) #abcdef

# Valid numeric strings can be converted
print(int("123") + int("123")) #246

# And numbers can be converted to strings
print(str(123) + str(123)) #123123

# In rare cases you may need the ASCII value of a char
print(ord("a")) #97
print(ord("b")) #98

# combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings)) #abcdef
