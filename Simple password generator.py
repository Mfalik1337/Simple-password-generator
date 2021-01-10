from string import printable
from random import choice

print ('Simple Password Generator by Mfalik1337')

while True:
    password = ''.join( [ choice(list( printable )) for x in range(int(input("Length: "))) ] )
    print("Password: {}".format(password.replace('\n', '@')))