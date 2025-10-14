header = """ bookstore 
customer receipt """

item1 = "book titile: {a} and price: {b}".format(a="Python Basics" , b= 450)
item2 = "book titile: {a} and price: {b}".format(a="Data Science Intro" , b= 600)

total = 450 + 600

thank_you = "Thank you for shopping with us"

recipt = header + "\n" + item1 + "\n" + item2 + "\n" + "Total: " + str(total) + "\n" + thank_you

print(recipt.upper())