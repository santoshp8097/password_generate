
'''
import random
def strong():
    upper = "ABCDEFGHIJKLMNOPQRSTUVW"
    lower = 'abcdefghijkl,mnopqrst'
    special = "!@#$%^&**"
    password = ''
    password += random.choice(upper)
    password += random.choice(lower)
    password += random.choice(special)
    password += random.choice (upper)
    return password

def weak():
    a = ['1234','abcd']
    return random.choice(a)

b = input("strong or weak = ")
if b == 'strong':
    print(strong())
    a=input("enter the number:")


elif b == 'weak':
    print(weak())
else:
    print("error")

=
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)

'''
'''print("generate password")
a = "!@#$%^&*"
b = "abcdefghijak"
password = ''
a=input("enter the password you want: ")
print(password)
print("your password is = ",a)'''



#password from input user
import string
from random import *
Character=string.ascii_letters+string.digits+string.punctuation
password=("".join(choice(Character)for i in range(randint(8,16))))
print(password)