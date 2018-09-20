import re
p = input ("Please! Enter your password")
x = True
while x :
    if (len(p) <6 or len(p) > 12):
        break
    elif not re.search ("[a-z]",p):
        break
    elif not re.search ("[0-9]",p):
        break
    elif not re.search ("[A-Z]",p):
        break
    elif not re.search ("[#$@]",p):
        break
    elif not re.search ("\s",p):
        break
    else:
        print("Congrats! This si a valid password")
        x = False
        break
if x:
    print ("Sorry! your password is incorrect")
#while loop  used when a condition is to be repeated in code form forever
#