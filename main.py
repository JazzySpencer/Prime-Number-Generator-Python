print("Please enter a number: ")
initnum = int(input())
if (initnum % 2) == 0:
    initnum += 1
    print("why u put even number")
else:
    print("at least u know it has to be odd")
dividingvalue = int(initnum / 3)
a = []
is_True = False
while is_True == False:
    for i in range(3, dividingvalue):
        a.append(initnum % i)
    if (a.count(0) == 0):
        is_True = True
        print(initnum)
    else:
        initnum += 2
        print(dividingvalue)
        a = []