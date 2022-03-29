''' 'does.txt' does not exist and we try to open it will go to exception handling '''
'''try:
    f = open("does.txt")
except Exception as e:
    print(e)
print("This line is important")'''

''' 'does.txt' does not exist and we try to open it again it will go to exception handling
but after that it will go to 'finally' '''
''' either it will go to 'except' or not but 'finally' will run definitely '''
'''f1 = open("mayank.txt")
try:
    f = open("does.txt")
except Exception as e:
    print(e)
finally:
    f1.close()
    print("Run this anyway...")
print("This line is important")'''


''' In this either it will go to 'except' or either in 'else' but after that it will go into 'finally' '''
'''f1 = open("mayank.txt")
try:
    f = open("sakshi_food.txt")
except Exception as e:
    print(e)
else:
    f.close()
    print("This will run only if except is not running")
finally:
    f1.close()
    print("Run this anyway...")
print("This line is important")'''

''' In this we find error type '''
f1 = open("mayank.txt")
try:
    f = open("sakshi_food.txt")
except EOFError as e:
    print("Print EOF error aagya", e)
except IOError as e:
    print("Print IO error aagya", e)
else:
    f.close()
    print("This will run only if except is not running")
finally:
    f1.close()
    print("Run this anyway...")
print("This line is important")