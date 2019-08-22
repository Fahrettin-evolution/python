number1 =int(input("need a number="))
number2 =int(input("need a number other="))
print("number1=",number1,"number2",number2)
number3=number1
number1=number2
number2=number3
print("number1=",number1,"number2=",number2)

#practical method
number1,number2=number2,number1
print("number1=",number1,"number2=",number2)
