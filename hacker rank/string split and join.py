
def string_split_join(s):
    s=s.split(" ")
    s="-".join(s)
    return s

s=str(input("enter the string: "))
print(string_split_join(s))
