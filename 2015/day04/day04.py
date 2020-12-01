import hashlib

# input = 'pqrstuv'
input = 'ckczppom'

found = False
num = 0
while not found:
    result = hashlib.md5((input + str(num)).encode()).hexdigest()
    if result[:6] == '000000':
        found = True
        print(num)
    num += 1

# print(hashlib.md5('abcdef609043'.encode()).hexdigest())
# print(str(1234))