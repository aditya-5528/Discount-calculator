lst = []  # an empty list we created

# number of elements as input
n = int(input("Enter number of products >>"))

# iterating till the range
for i in range(0, n):
    ele = int(input("Enter the product prices >>"))

    lst.append(ele)  # adding the element

total = 0 #ie the total amount customer purchased

for i in range(0, len(lst)): ## iterating till the range i.e length of list
    total = total + lst[i]


if total >= 1000: #if condition that if amount is greater than or equal 1000
    print(f"you are eligible  for 10% cash discount on ${total}")
    amount_paid = total * 90/100 # amount after discount of 10%
    print(f"Your total amount after the discount is ${amount_paid}")
else:  #else condition that if amount is smaller than 1000
    print("Sorry your total price is bellow $1000, so you are not eligible for cash discount. ")
    print(f"your payable amount is ${total}")