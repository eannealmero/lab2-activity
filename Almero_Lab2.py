# The program should calculate and display the total cost of the three items.
first = float(input("Enter amount of first purchase: "))
second = float(input("Enter amount of second purchase: "))
third = float(input("Enter amount of third purchase: "))
totalpurchase = first + second + third
print(f"Total Purchase is: ₱{totalpurchase:.2f} ")

# #Display a message to the customer if they qualify for a discount. To qualify, the total cost purchased must exceeds 100.00, a 10% discount is applied.
discount = 0
if totalpurchase > 100.00:
    print("You are qualified for a discount.")
    discount = totalpurchase * 0.10
    newtotal = totalpurchase - discount
    print(f"Discount applied: ₱{discount:.2f}")
else:
    print("You are not qualified for a discount.")
    newtotal = totalpurchase

# #The program should calculate loyalty points, awarding 1 point for every 10.00 spent 
loyalty = newtotal // 10.00
print(f"Final Total: ₱{newtotal:.2f}")
print(f"Loyalty Points Earned: {loyalty:.0f}")

#Display the final total price and the number of loyalty points 
#Enter payment and accept only if it's greater than the total purchased. Display change if applicable.
payment = float(input("Enter Payment: "))
if payment >= newtotal:
    change = payment - newtotal
    print(f"Your change is: ₱{change:.2f}")
else:
    print("Payment is Insufficient.")
