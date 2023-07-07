Practical
# 1 Write thefollowing
programs
for in Python:
    (I)
    A
    simple
    client


    class that generates the private and public keys by using the built in Python RSA algorithm and
test
it
(II)
A
transaction


class to send and receive money and test it.

# import libraries


import hashlib

import

binascii
import

numpy as np
import

pandas as pd
import

pylab as pl
import

logging
import

datetime
import

collections
pip
install
pycryptodome
# following imports are required by PKI
import Crypto.Random
from

Crypto.Hash
from

Crypto.PublicKey
import RSA
from

Crypto.Signature
import PKCS1_v1_5

import binascii


class Client: def


__init__(self):

random = Crypto.Random.new().read
self._private_key = RSA.generate(1024, random)
self._public_key = self._private_key.publickey()
self._signer = PKCS1_v1_5.new(self._private_key)


@property def
    identity(self):


return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


class Transaction:


def __init__(self,

             sender, recipient, value):
    self.sender = sender


self.recipient = recipient
self.value = value
self.time = datetime.datetime.now()


def to_dict(self):


if self.sender ==

"Genesis":
identity = "Genesis"
else:
identity = self.sender.identity
return collections.OrderedDict({
    'sender': identity,
    'recipient': self.recipient,
    'value': self.value,
    'time': self.time})


def


sign_transaction(self):
private_key = self.sender._private_key

signer = PKCS1_v1_5.new(private_key)

h =

SHA.new(str(self.to_dict()).encode('utf8'))

return

binascii.hexlify(signer.sign(h)).decode('ascii')
Dinesh = Client()
Ramesh = Client()
t =
Transaction(Dinesh, Ramesh.identity, 5.0)
signature = t.sign_transaction()
print
(signature)
Output:

Practical
2
Write
the
following
programs
for in Python:
    (I).Create
    multiple
    transactions and display
    them.
(II).Create
a, a
genesis
block and execute
it.


def display_transaction(transaction):


# for transaction in transactions:
dict = transaction.to_dict()
print
("sender: " + dict['sender'])
print
('-----')
print("recipient: " + dict['recipient'])
print('-----')
print("value: " + str(dict['value']))
print('-----')
print("time: " + str(dict['time']))
print('-----')

transactions = []

Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()

t1 = Transaction(
    Dinesh,
    Ramesh.identity,
    15.0
)

t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(
    Dinesh,
    Seema.identity,
    6.0
)
t2.sign_transaction()
transactions.append(t2)
t3
= Transaction(

    Ramesh,

    Vijay.identity,
    2.0
)
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(
    Seema,
    Ramesh.identity,
    4.0
)
t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(Vijay,
                 Seema.identity,
                 7.0
                 )

t5.sign_transaction()
transactions.append(t5)
t6
= Transaction(

    Ramesh,

    Seema.identity,
    3.0
)
t6.sign_transaction()
transactions.append(t6)
t7 = Transaction(
    Seema,
    Dinesh.identity,
    8.0
)
t7.sign_transaction()
transactions.append(t7)
t8 = Transaction(
    Seema,
    Ramesh.identity,
    1.0
)
t8.sign_transaction()
transactions.append(t8)
t9
= Transaction(
    Vijay,
    Dinesh.identity,
    5.0
)

t9.sign_transaction()
transactions.append(t9)
t10
= Transaction(
    Vijay,
    Ramesh.identity,
    3.0
)
t10.sign_transaction()
transactions.append(t10)

for transaction in transactions:
    display_transaction(transaction)
    print
('--------------')


class Block: def


__init__(self):
self.verified_transactions = []
self.previous_block_hash = ""

self.Nonce

= ""

last_block_hash = ""

Dinesh = Client()

t0 = Transaction(
    "Genesis",
    Dinesh.identity,
    500.0
)
block0 = Block()

block0.previous_block_hash = None
Nonce = None

block0.verified_transactions.append(t0)

digest = hash(block0)
last_block_hash = digest

TPCoins = []


def dump_(self):
    print("Number of blocks in the chain: " + str(len(self)))


for x in range(len(TPCoins)):
    TPCoins[x]

block_temp =

print("block # " + str(x))

for

transaction in block_temp.verified_transactions:
display_transaction(transaction)
print('--------------')
print('=====================================')

TPCoins.append(block0)
dump_(TPCoins)
Output:

Practical
3
Write
the
following
programs
for in Python:
    (I).Create
    a
    mining
    function and test
    it.
(II).Add
blocks
to
the
miner and dump
the.


def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()


def mine(message, difficulty=1):
    assert difficulty >= 1


prefix = '1' * difficulty
for
    i in range(1000):
digest = sha256(str(hash(message)) + str(i))
if digest.startswith(prefix):
    print("after " + str(i) + " iterations found nonce: " + digest)
return digest

last_transaction_index = 0

block = Block()
for
    i in range(3):
temp_transaction = transactions[last_transaction_index]
# validate transaction
# if valid
block.verified_transactions.append
last_transaction_index

+=

1

(temp_transaction)
mine

("test

 message",

 2)

block.previous_block_hash = last_block_hash
block.Nonce = mine(block, 2)
digest = hash(block)
TPCoins.append(block)
last_block_hash = digest

# Miner 2 adds a block
block = Block()

for i in range(3):

temp_transaction =

transactions[last_transaction_index]
# validate transaction
# if valid
block.verified_transactions.append(temp_transaction)
last_transaction_index += 1
block.previous_block_hash
= last_block_hash
block.Nonce = mine(block, 2)
digest
= hash(block)
TPCoins.append(block)
last_block_hash
= digest  # Miner 3 adds a block block = Block()

for i in range(3):
    temp_transaction = transactions[last_transaction_index]
# display_transaction (temp_transaction)
# validate transaction
# if valid
block.verified_transactions.append(temp_transaction)
last_transaction_index += 1

block.previous_block_hash = last_block_hash
block.Nonce = mine(block, 2)
digest = hash
(block)

TPCoins.append(block)
last_block_hash = digest
dump_(TPCoins)
Full
Output:

Practical
4
Implement and demonstrate
the
use
of
the
following in Solidity:
(I).Varaible
(II).Operators
(III).Loops
(IV).Decision
Making
(V).Strings

(I).Variable
pragma
solidity ^ 0.5
.0;
contract
SolidityTest
{uint
storedData; // State
variable
constructor()
public
{
    storedData = 10;
}
function
getResult()
public
view
returns(uint)
{
    uint
a = 1; // local
variable
uint
b = 2;
uint
result = a + b;
return storedData; // access
the
state
variable
}
}

Output:

// Solidity
program
to
demonstrate
state
variables
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
Solidity_var_Test
{
// Declaring
a
state
variable
uint8
public
state_var;

// Defining
a
constructor
constructor()
public
{
state_var = 16;
}
}

Output:

// Solidity
program
to
show
Global
variables
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
Test
{

// Defining
a
variable
address
public
admin;

// Creating
a
constructor
to
// use
Global
variable
constructor()
public
{admin
= msg.sender;
}}
Output:

(II).Operators
// Solidity
contract
to
demonstrate
Arithematic
Operator
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
SolidityTest
{

// Initializing
variables
uint16
public
a = 20;
uint16
public
b = 10;
// Initializing
a
variable
with sum uint
public sum = a + b;

// Initializing a variable with the difference uint
public diff = a - b;

// Initializing a variable with product uint
public mul = a * b;

// Initializing a variable with quotient uint
public div = a / b;

// Initializing a variable with modulus uint
public mod = a % b;

// Initializing a variable decrement value uint
public dec = --b;

// Initializing a variable with increment value uint
public inc = ++a;
}
Output:

    (IV).Decision
Making
// Solidity
program
to
demonstrate
the
use
of
'if statement'
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
Types
{ //
Declaring
state
variable
uint
i = 10;

// Defining
function
to
demonstrate
use
of
'if statement'
function
decision_making()
public
view
returns(bool)
{
if (i < 10){
return true;
}
}}
Output:

// Solidity
program
to
demonstrate
the
use
of
'if...else'
statement
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
Types
{

// Declaring
state
variables
uint
i = 10;
bool
even;

// Defining
function
to
// demonstrate
the
use
of
// 'if...else statement'
function
decision_making()
public
{ if (i % 2
== 0){even = true;} else {even =
false;
}}
function
getresult()
public
view
returns(bool)
{
return
even;
}

}

Output:

(III)

Strings

//

Solidity

program
to
demonstrate //
how
to
create
a
contract
pragma
solidity ^ 0.4
.23;

// Creating
a
contract
contract
Test
{

// Declaring
variable
string
str;

// Defining
a
constructor
constructor(string
str_in){
str = str_in;
}

// Defining
a
function
to
//
return value
of
variable
'str'
function
str_out()
public
view
returns(string
memory){
return str;
}
}
O
ut
pu
t

Practical
5
Implement and demonstrate
the
use
of
the
following in Solidity:
(I).Arrays
(II).Enums
(III).Structs
(IV).Mappings
(V).Coversations
(VI).Ether
Units
(VII).Special
Varaibles

(I).Arrays
// Solidity
program
to
demonstrate
// creating
a
fixed - size
array
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
Types
{

// Declaring
state
variables
// of
type
array
uint[6]
data1;
int[5]
data;

// Defining
function
to
add
// values
to
an
array
function
array_example()
public
returns(int[5]
memory, uint[6]
memory){data
= [int(50), -63, 77, -28, 90];
data1 = [uint(10), 20, 30, 40, 50, 60];
}
function
getresult()
public
view
returns(int[5]
memory, uint[6]
memory){
return
(data, data1);
}}
Output:

(III).Structs

pragma
solidity ^ 0.5
.0;
contract
test
{
    struct
Book
{
string
title;
string
author;
uint
book_id;
}
Book
book;
function
setBook()
public
{book
= Book('Learn Java', 'TP', 1);
}
function
getBookId()
public
view
returns(uint)
{
return
book.book_id;
}
}

Output:

(IV).Mappings
pragma
solidity ^ 0.5
.0;
contract
LedgerBalance
{mapping(address= > uint)
balance;
function
updateBalance()
public
returns(uint)
{balance[msg.sender] = 20;
return
balance[msg.sender];
}}
Output:

pragma
solidity ^ 0.5
.0;
contract
LedgerBalance
{
    mapping(address= > string) name;

function
updateBalance()
public
returns(string
memory){
name[msg.sender] = "Dip";
return name[msg.sender];
}
function
printsender()
public
view
returns(address)
{
return
msg.sender;
}}
Output:

Practical
6
Implement and demonstrate
the
use
of
the
following in Solidity:
(I).Functions
(II).View
Functions
(III).Pure
Functions
(IV).Fallback
Functions
(V).Function
Overloading
(VI).Mathematical
Functions
(VII).Cryptographic
Functions

(I).Functions
pragma
solidity ^ 0.5
.0;
contract
SolidityTest
{
    function
testpgmresult()
public
view
returns(uint)
{
uint
a = 1000; // local
variable
uint
b = 2000;
uint
result = a + b;
return result; // access
the
state
variable
}
}

Output:

(II).View
Functions
pragma
solidity ^ 0.5
.0;
contract
Test
{
    function
getResult()
public
view
returns(uint
product, uint
sum){
uint
a = 1; // local
variable
uint
b = 2;
product = a * b;
sum = a +
b;
}
}
O
ut

pu
t:

(III).Pure
Functions
pragma
solidity ^ 0.5
.0;
contract
C
{ // private
state
variable
uint
private
data;

// public
state
variable
uint
public
info;

// constructor
constructor()
public
{info
= 10;
}
// private
function
function
increment(uint
a) private
pure
returns(uint)
{
return a + 1;}

// public
function
function
updateData(uint
a) public
{data = a;} function
getData()
public
view
returns(uint)
{
return data;} function
compute(uint
a, uint
b) internal
pure
returns(uint)
{
return a + b;}
}

// Derived
Contract
contract
E is C
{
    uint
private
result;
C
private
c;

constructor()
public
{
c = new
C();}
function
getComputedResult()
public
{result
= compute(3, 5);
}
function
getResult()
public
view
returns(uint)
{
return result;} function
getData()
public
view
returns(uint)
{
return c.info();}
}
Output:

(V).Function

Overloading

pragma
solidity ^ 0.5
.0;
contract
Test
{
    function
getSum(uint
a, uint
b) public
pure
returns(uint)
{
return
a + b;
}
function
getSum(uint
a, uint
b, uint
c) public
pure
returns(uint)
{
return
a + b + c;
}
function
callSumWithTwoArguments()
public
pure
returns(uint)
{
return
getSum(1, 2);
}
function
callSumWithThreeArguments()
public
pure
returns(uint)
{
return
getSum(1, 2, 3);
}
}

Output:

(VI).Mathematical
Functions
pragma
solidity ^ 0.5
.0;
contract
Test
{
    function
callAddMod()
public
pure
returns(uint)
{
return
addmod(4, 5, 3);
}
function
callMulMod()
public
pure
returns(uint)
{
return
mulmod(4, 5, 3);
}
}

Output:

(VII).Cryptographic
Functions
pragma
solidity ^ 0.5
.0;
contract
Test
{
    function
callsha256()
public
pure
returns(bytes32
result){
return
sha256("ronaldo");
}
function
callkeccak256()
public
pure
returns(bytes32
result){
return
keccak256("ronaldo");
}
}

Output:

Practical
7
Implement and demonstrate
the
use
of
the
following in Solidity:
(I).Contracts
(II).Inheritance
(III).Constructors
(IV).Abstract
Class
(V).Interfaces

(I).Contracts
// Solidity
program
to //
demonstrate
how
to // write
a
smart
contract
pragma
solidity >=
0.4
.16 < 0.7
.0;

// Defining
a
contract
contract
Test
{

// Declaring
state
variables
uint
public
var1;
uint
public
var2;
uint
public
sum;

// Defining
public
function
// that
sets
the
value
of // the
state
variable
function
set(uint
x,
uint
y) public
{var1 = x;
var2 = y;
sum = var1 + var2;
}

// Defining
function
to
// print
the
sum
of
// state
variables
function
get(
) public
view
returns(uint)
{
return sum;
}
}

Output:

(II).Inheritance
// Solidity
program
to
demonstrate
Single
Inheritance
pragma
solidity >= 0.4
.22 < 0.6
.0;

// Defining
contract
contract
parent
{

// Declaring
internal
state
varaiable
uint
internal
sum;

// Defining
external
function
to
set
value
of
internal
state
variable
sum
function
setValue()
external
{uint
a = 10;
uint
b = 20;
sum = a + b;
}
}
// Defining
child
contract
contract
child is parent
{

// Defining
external
function
to
return value
of
internal
state
variable
sum
function
getValue()
external
view
returns(uint)
{
return sum;
}}
// Defining
calling
contract
contract
caller
{

// Creating
child
contract
object
child
cc = new
child();

// Defining
function
to
call
setValue and getValue
functions
function
testInheritance()
public
{cc.setValue();
}
function
result()
public
view
returns(uint)
{
return
cc.getValue();
}
}

Output:

(III).Constructors
// Solidity
program
to
demonstrate
// creating
a
constructor
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
constructorExample
{

// Declaring
state
variable
string
str;

// Creating
a
constructor
// to
set
value
of
'str'
constructor()
public
{str
= "GeeksForGeeks";
}

// Defining
function
to //
return the
value
of
'str'
function
getValue()
public
view
returns(
    string
memory) {
return
str;}
}
Output:
Practical
8

Implement and demonstrate
the
use
of
the
following in Solidity:
(I).Libraries
(II).Assembly
(III).Events
(IV).Error
Handling

(IV).Error
Handling

// Solidity
program
to
demonstrate
require
statement
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
requireStatement
{

// Defining
function
to
check
input
function
checkInput(uint
_input)
public
view
returns(string
memory){
require(_input >= 0, "invalid uint8");
require(_input <= 255, "invalid uint8");
return "Input is Uint8";
}

// Defining
function
to
use
require
statement
function
Odd(uint
_input) public
view
returns(bool)
{
require(_input % 2 != 0);
return true;
}
}

Output:

// Solidity
program
to
demonstrate
assert statement
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
assertStatement
{

// Defining
a
state
variable
bool
result;

// Defining
a
function
to
check
condition
function
checkOverflow(uint
_num1,
uint
_num2) public
{
uint8
sum = _num1 + _num2;
assert (sum <= 255);
result =
true;
}

// Defining
a
function
to
print
result
of
assert statement
function
getResult()
public
view
returns(string
memory){
if (result == true){
return "No Overflow";
} else {
return "Overflow exist";
}}
}
Output:

// Solidity
program
to
demonstrate
assert statement
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
assertStatement
{

// Defining
a
state
variable
bool
result;
// Defining
a
function //
to
check
condition
function
checkOverflow(uint8
sum) public
{
assert (sum <= 255);
result
= true;
}

// Defining
a
function
to
print
result
of
assert statement
function
getResult()
public
view
returns(string
memory){
if (result == true)
{
return "No Overflow";
} else {
return "Overflow exist";
}}
}

Output:

// Solidity
program
to
demonstrate
revert
statement
pragma
solidity ^ 0.5
.0;

// Creating
a
contract
contract
revertStatement
{

// Defining
a
function
to
check
condition
function
checkOverflow(
    uint
_num1, uint
_num2) public
view
returns(
    string
memory, uint) {uint
sum = _num1 + \
      _num2;
if (sum < 0 | | sum > 255)
{
revert(" Overflow Exist");
} else {
return ("No Overflow", sum);
}}
}
}
