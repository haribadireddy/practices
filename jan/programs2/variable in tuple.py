def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)


person(name="hari",age="28",city="rjy")