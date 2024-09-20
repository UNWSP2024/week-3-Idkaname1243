# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%.
# Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.
total = 0
hotdog = input("enter what kind of hotdog you want Hot Dog or Chilli Dog:   ")
if hotdog == ("Hot Dog") or ("hot dog") or ("hotdog"):
    total = total + 3.5
if hotdog == ("Chilli Dog") or ("chilli dog") or ("chillidog"):
    total = total + 4.5
  #this part is to take the hot dog type wanted and to add the price of it to the total
top1 = input("enter what kind of Hotdog topping you want (options are cheese, peppers, grilled onions):   ")
top2 = input("enter what kind of Hotdog topping you want (options are cheese, peppers, grilled onions):   ")
top3 = input("enter what kind of Hotdog topping you want (options are cheese, peppers, grilled onions):   ")
#this part takes the toppings wanted by the 'customer'
if top1 == ("cheese") or ("Cheese"):
    total = total + 0.5
if top1 == ("peppers") or ("Peppers"):
    total = total + 0.75
if top1 == ("grilled onions") or ("Grilled Onions"):
    total = total + 1
if top2 == ("cheese") or ("Cheese"):
    total = total + 0.5
if top2 == ("peppers") or ("Peppers"):
    total = total + 0.75
if top2 == ("grilled onions") or ("Grilled Onions"):
    total = total + 1
if top3 == ("cheese") or ("Cheese"):
    total = total + 0.5
if top3 == ("peppers") or ("Peppers"):
    total = total + 0.75
if top3 == ("grilled onions") or ("Grilled Onions"):
    total = total + 1
print("your total is " + str(total))
taxtotal = (total*0.07)
rtaxtotal = round(taxtotal,2)
#this part is to change the total to add the toppings price
print("your total after tax is " + str(rtaxtotal))
