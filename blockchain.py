#! /bin/python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import hashlib
import random

alice_key = RSA.generate(1024)
bob_key = RSA.generate(1024)

block_0 = open('block_0','w')
block_0.write('alice, 10, btc\nbob, 10, btc')
block_0.close()

transaction_1 = b'alice_send_10_to_bob'
transaction_2 = b'bob_send_3_to_alice'

encryptor = PKCS1_OAEP.new(alice_key)
signed_t1 = encryptor.encrypt(transaction_1)
signed_t2 = encryptor.encrypt(transaction_2)

block_1 = open('block_1', 'w')
block_1.write(str(transaction_1))
block_1.write(',')
block_1.write(str(signed_t1))
block_1.write('\n')
block_1.write(str(transaction_2))
block_1.write(',')
block_1.write(str(signed_t2))
block_1.write('\n')
block_1.close()

def hash(filename) : 
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        return(readable_hash)
    
while True :
    block_1 = open('block_0', 'a')
    block_1.write(str(random.randint(0,1)))
    block_1.close()
    h = str(hash('block_0'))[0:5]
    print(h)
    if h == '00000':
        ok = 1
        break

block_1 = open('block_1', 'a')
block_1.write('\n')
block_1.write(str(hash('block_1')))
block_1.close()
