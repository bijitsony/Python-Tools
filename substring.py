s = 'abcbabcdf'
r = ''
c = ''
for char in s:
    if (c == ''):
        c = char
        print (char)
    elif (c[-1] <= char):
        c += char
        print (" ", char)
    elif (c[-1] > char):
        if (len(r) < len(c)):
            r = c
            c = char
        else:
            c = char
        print("  ", char)
if (len(c) > len(r)):
    r = c
print(r)
