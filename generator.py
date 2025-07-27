
import random
import string

# options for characters are letters (upper and lower) and integers.

chars = string.ascii_letters + string.digits

# randomly select 32 characters to create password.

password = ''.join([random.choice(chars) for x in range(32)])

# print resulting password.

print('password', password)

