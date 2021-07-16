from web3 import Web3 
import json

# Run with python app_3.py 

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Gets the first account on Ganache 
web3.eth.defaultAccount = web3.eth.accounts[0]


# Got this from Remix details in compiler. Web3 Deploy

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

address = web3.toChecksumAddress("0x9c463dE9e8b5922989E023D521D7A5D8E0Db0217")

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())

# Writing back 
tx_hash = contract.functions.setGreeting('CHEA BRAH!').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated greeting: {}'.format(
	contract.functions.greet().call()
))

