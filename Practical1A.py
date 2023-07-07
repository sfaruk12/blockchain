# A simple client class that generates the private and public keys by using the built in Python RSA algorithm and test it
# import libraries import hashlib import random import string import json import binascii import numpy as np import pandas as pd import pylab as pl import logging import datetime import collections
# pip install pycryptodome
# following imports are required by PKI import Crypto import Crypto.Random from Crypto.Hash import SHA from Crypto.PublicKey import RSA from Crypto.Signature import PKCS1_v1_5


import binascii


class Client: def


__init__(self):

random = Crypto.Random.new().read
self._private_key = RSA.generate(1024, random)
self._public_key = self._private_key.publickey()
self._signer = PKCS1_v1_5.new(self._private_key)


@property def identity(self):
    return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


class Transaction: def


__init__(self, sender, recipient, value):
self.sender = sender
self.recipient = recipient
self.value = value
self.time = datetime.datetime.now()


def to_dict(self): if


self.sender == "Genesis":
identity = "Genesis" else:
identity = self.sender.identity
return collections.OrderedDict({
    'sender': identity,
    'recipient': self.recipient,
    'value': self.value, 'time': self.time})


def sign_transaction(self):
    private_key = self.sender._private_key


signer = PKCS1_v1_5.new(private_key)
h = SHA.new(str(self.to_dict()).encode('utf8'))
return binascii.hexlify(signer.sign(h)).decode('ascii')
Dinesh = Client()
Ramesh = Client()
t = Transaction(Dinesh, Ramesh.identity, 5.0)
signature = t.sign_transaction()
print
