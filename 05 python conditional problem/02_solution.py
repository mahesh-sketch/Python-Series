def TicketBooking(age,day):
    price = 12 if age >= 18 else 8
    
    if(day == 'wed' or day == 'Wed'):
        price-=2
        print("Your Ticket Price is:$",price)
    else:
        print('Your Ticket price is :$',price)

age = int(input("Enter your Age:"))
day = str(input("Enter your day:"))
TicketBooking(age,day)