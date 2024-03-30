import random
import string

def GreetUser(name):
    if name:
        print("Hello Namaste " + name + "🙏" )
    else:
        random_names = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        print("Hello Namaste " + random_names + "🙏")

username = input("Enter your name: ")
GreetUser(username)
