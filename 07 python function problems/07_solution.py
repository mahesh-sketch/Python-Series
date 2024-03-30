def Sum(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)
    

print("Sum is: ",Sum(2,2,3))