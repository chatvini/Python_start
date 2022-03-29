# Exercise 2 faulty calculator
'''design a calculator which will correctly solve all the problems except the following ones:
45*3=555, 56+9=77, 56/6=4 '''
'''Your program should take operator and the two number as input and then return the result'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operat = input("Enter operator : ")
loop_val = 1


if num1==45 and num2==3 and operat=="*":
    print("555")
elif num1==56 and num2==9 and operat=="+":
    print("77")
elif num1==56 and num2==6 and operat=="/":
    print("4")
elif operat=="*":
    mult = num1*num2
    print(mult)
elif operat=="+":
    plus = num1+num2
    print(plus)
elif operat=="/":
    divide = num1/num2
    print(divide)
elif operat=="-":
    minus = num1-num2
    print(minus)
else:
    print("Unexpected error")