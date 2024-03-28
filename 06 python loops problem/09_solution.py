def Duplicate(numlist):
    unique_item = set()
    for item in numlist:
        if item in unique_item:
            print("Dupliacte: ", item)
            break
        unique_item.add(item)
    


numlist = [int(item) for item in input("Enter the element: ").split()]
Duplicate(numlist)
     