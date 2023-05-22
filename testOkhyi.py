def cacul():
    num1= int(input("write first number:"))

    num2 = int(input("write second number?:")) 
    ope = input("add, sub, div, min :")

    if ope=="add":
        print(num1+num2)
    elif ope=="sub":
        print(num1*num2)
    elif ope=="div":
        print(num1/num2)
    elif ope=="min":
        print(num1-num2)
choice=True    
while choice:
    cacul()
    reponse= input("do you want to continue?(y/n)")
    if reponse=="n":
        choice=False
print("Fin")
        




