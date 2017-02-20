import bcrypt
from time import time

password = b'Very secret password'

start = time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt(15))
print('Runtime: ', time() - start)

print(hashed)

# check password
if bcrypt.hashpw(password, hashed) == hashed:
    print( 'It matches')
else:
    print('It does not match')