
try:
    a= 10
    b= int(input("Enter the number"))
    c=a/b
    print("Division Output:", c)
except:
    print("There is a division error, May be the entered number is zero and division by zero results in infinity which can't be displayed ")
finally:
    print("Division Complete")





