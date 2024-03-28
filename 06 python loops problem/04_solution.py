# Reverse a string using a loop.

def ReverseString(strs):
    revstring = ""
    for i in strs:
        revstring = i + revstring
    
    print("Reverse String is: " + revstring)

name = str(input("Enter your String: "))
ReverseString(name)