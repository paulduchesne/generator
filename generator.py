
import random
import string

# options for characters are letters (upper and lower) and integers.

chars = string.ascii_letters + string.digits

# randomly select 16 characters to create password.

password = ''.join([random.choice(chars) for x in range(16)])

# print resulting password.

print('password', password)

