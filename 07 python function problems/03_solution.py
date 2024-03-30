def multiply(p1, p2):
    if isinstance(p1, str) or isinstance(p2, str):
        return (p1) * (p2)
    else:
        return p1 * p2

print(multiply(8, 5))    
print(multiply('a', 5))  
print(multiply(5, 'a'))  
