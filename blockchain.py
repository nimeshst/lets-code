#lets learn blockchain by building one
#blockchain is an immutable sequence of block linked togetherusing hashes
#bockchain is technology behind bitcoin 
#block contains data which could be anything like files ,transactions and so on

import hashlib

import time 
class Block(object):

    def __init__(self ,index,proof_number,previous_hash ,data ,timestamp=None ):
        self.index=index#track the position block within the blockchain
        self.proof_number=proof_number#proof of work
        self.previous_hash =previous_hash#hash of the previous value
        self.data=data#store the details of the transaction
        self.timestamp=time.time()
    
    def compute_hash(self):
        string_block ="{}{}{}{}{}".format(self.index,self.proof_number,self.previous_hash)
        return hashlib.sha256(string_block.encode()).hexdigest()

    def __repr__(self):
        return "{}-{}-{}-{}-{}".format(self.index,self.proof_number,self.previous_hash,self.data,self.timestamp)

class Bock_chain(object):
    def __init__(self):
        self.chain=[]#stores all the block

        self.current_data=[]#stores the infromation about the transaction of the block
        self.nodes=set()
        self.build_genesis()#use to build the initial block of the chain

    def build_genesis(self):
        
        #is the first block of the chain and we have to initialze it with a hash 
        #we use build block and give a default value
        self.build_block(proof_number=0,previous_hash=0)

    def build_block(self,proof_number,previous_hash):
        block=Block(index =len(self.chain),proof_number=proof_number,previous_hash ,data=self.current_data)
        self.current_data=[]
        self.chain.append(block)
        return block
    #hashes are important in block chain to determine the validity of each block
    #therefore confrim_validity method utilizes a series of if statements to assess 
    #whether the hash of each block is compromised or not 

    def confirm_validity(block,previous_block):
        if previous_block.index +1!=block.index:
            return False
        elif previous_block.compute_hash !=block.previous_hash:
            return False
        elif block.timestamp<=previous_block.timestamp:
            return False
        return True

    def get_data(self,sender,receiver,amount):
        #takes 3 parametes( sender ,receiver,amount ) and adds the transaction data to the list
        self.current_data.append({
            'sender':sender,
            'receiver':receiver,
            'amount':amount
            })
        return True
    def block_mining (self,details_miner):
        self.get_data(
                sender="0"
                receiver=details_miner,
                quantity=1,#creating a new block (or identifying the proof number)is awarded with 1
                )
        last_block=self.latest_block
        last_proof_number=last_block.proof_number
        proof_number =self.proof_of_work(last_proof_number)
        last_hash =last_block.compute_hash
        block=self.build_block(proof_number,last_hash)

        return vars(block)
    
    def latest_block(self):
        return self.chain[-1]

    
    def create_node(self,address):
        self.nodes.add(address)
        return True

    def get_block_object(block_data):
        return Block(
            block_data['index'],
            block_data['proof_number']
            block_data['previous_hash']
            block_data['timestamp']
                )


block_chain=Blockchain()
#mining about to start
print(block_chain.chain)
last_block=blockchain.latest_bock
last_proof_number=last_block.proof_number
proof_number=block_chain.proof_of_work(last_proof_number)
block_chain.get_data(
        sender="0",
        receiver="receiver",
        amount=1
        
        )
last_hash=last_block.compute_hash
block= blockchain.build_block(proof_number,last_hash)

print("mining sucessfull")

