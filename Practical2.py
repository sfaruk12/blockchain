# (I).Create multiple transactions and display them .
# (II). Create a blockchain, a genesis block and execute it .
def display_transaction(transaction):
    # for transaction in transactions: dict = transaction.to_dict() print ("sender: " + dict['sender']) print ('-----')
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
t1 = Transaction(Dinesh,
                 Ramesh.identity,
                 15.0
                 )
t1.sign_transaction()
transactions.append(t1)
t2 = Transaction(Dinesh,
                 Seema.identity,
                 6.0
                 )
t2.sign_transaction()
transactions.append(t2)
t3 = Transaction(Ramesh,
                 Vijay.identity,
                 2.0
                 )
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(Seema,
                 Ramesh.identity,
                 4.0
                 )
t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(Vijay,
                 Seema.identity,
                 7.0
                 )
M.Sc.IT(Sem - 4)
Blockchain
Akbar
Peerbhoy
college
of
Commerce and Economics
Prof
Eram
Qureshi
t5.sign_transaction()
transactions.append(t5)
t6 = Transaction(Ramesh,
                 Seema.identity,
                 3.0
                 )
t6.sign_transaction()
transactions.append(t6)
t7 = Transaction(Seema,
                 Dinesh.identity,
                 8.0
                 )
t7.sign_transaction()
transactions.append(t7)
t8 = Transaction(Seema,
                 Ramesh.identity,
                 1.0
                 )
t8.sign_transaction()
transactions.append(t8)
t9 = Transaction(
    Vijay,
    Dinesh.identity,
    5.0
)
M.Sc.IT(Sem - 4)
Blockchain
Akbar
Peerbhoy
college
of
Commerce and Economics
Prof
Eram
Qureshi
t9.sign_transaction()
transactions.append(t9)
t10 = Transaction(
    Vijay,
    Ramesh.identity,
    3.0
)
t10.sign_transaction()
transactions.append(t10)
for transaction in transactions: display_transaction(transaction)
print('--------------')


class Block: def


__init__(self):
self.verified_transactions = []
self.previous_block_hash = ""
self.Nonce = ""
last_block_hash = ""
Dinesh = Client()
t0 = Transaction(
    "Genesis",
    Dinesh.identity,
    500.0
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

for transaction in block_temp.verified_transactions:
    display_transaction(transaction)
print('--------------')
print('=====================================')

TPCoins.append(block0)
dump_(TPCoins)


class Client:
    def __init__(self):
        # Define the attributes of the Client class here
        self.identity = self.generate_identity()

    def generate_identity(self):
        # Implement the logic to generate a unique identity for the client
        pass


class Transaction:
    def __init__(self, sender, recipient, value):
        # Define the attributes of the Transaction class here
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = self.generate_time()
        self.signature = None

    def generate_time(self):
        # Implement the logic to generate the transaction time
        pass

    def sign_transaction(self):
        # Implement the logic to sign the transaction
        pass


class Block:
    def __init__(self):
        # Define the attributes of the Block class here
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.nonce = ""

    def add_transaction(self, transaction):
        # Implement the logic to add a transaction to the block
        pass

    def generate_hash(self):
        # Implement the logic to generate the hash of the block
        pass

    def mine_block(self, difficulty):
        # Implement the logic to mine the block with the given difficulty level
        pass
