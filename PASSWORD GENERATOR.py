import random
import string
length=10
password="".join(random.choices(string.ascii_letters+string.digits+string.hexdigits,k=length))
print("random generated password of length",length,":",password)
