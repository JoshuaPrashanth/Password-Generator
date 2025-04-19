import random
import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
num = string.digits
spchar = string.punctuation

length = 12
password = ''
variables = lowercase + uppercase + num + spchar
for i in range(length):
    password += random.choice(variables)
print(password)

