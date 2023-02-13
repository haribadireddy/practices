"""s = input()
pos = int(input())
char = input()
l = list(s)
l[pos] = char
s = "".join(l)
print(s)"""


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

"""s = "abrcadabra"
l = list(s)
l[5] = 'k'
s = ''.join(l)
print(s)"""
