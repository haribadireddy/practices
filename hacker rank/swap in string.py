def swap_case_for_letter_old(i):
    new = ''
    if i == "A":
        new = "a"
        return new
    if i == "B":
        new = "b"
        return new
    if i == "B":
        new = "b"
        return new
    if i == "C":
        new = "c"
        return new
    if i == "D":
        new = "d"
        return new
    if i == "E":
        new = "e"
        return new


def swap_case_for_letter(c):
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return c.lower()
    elif c in "abcdefghijklmnopqrstuvwxyz":
        return c.upper()
    else:
        return c


def swap_case_for_letters(c):
    o = ord(c)
    if 122 >= o >= 97:
        return chr(o - 32)
    elif 90 >= o >= 65:
        return chr(o + 32)
    else:
        return c


def swap_case(input):
    output = ""
    for c in input:
        output += swap_case_for_letters(c)
        # print(output)
    return output


s = str(input())
result = swap_case(s)
print(result)
