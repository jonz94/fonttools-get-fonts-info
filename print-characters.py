s = ""

for c in (
    list(range(32, 48))
    + list(range(58, 65))
    + list(range(91, 97))
    + list(range(123, 127))
):
    print(chr(c))
    s = s + chr(c)

print(s)
