from web3 import Web3 

# Run with python app_2.py

# How to build a transaction in python using Ganance and send crypto currency with web 3 and python. 


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Send Eth from account 1 to account 2 

account_1 = "0x2c5C6592F3BAd46f3091D4e19CCE2C9b7260050D"
account_2 = "0x874025e58EB375D3A0cd643C35dAe777E6341CF7"

# We need a private key to tell web3 that its ok that we send crypto between accounts 

private_key = "4598058c078df3420dde4202ca2d37d47b43ac1cf875219a30367d3b6038f479" # password. 

# get the nonce, nonce stops you sending transaction twice
nonce = web3.eth.getTransactionCount(account_1)

# build a transaction
tx = {
	'nonce':nonce, 
	'to':account_2,
	'value':web3.toWei(1,'ether'),
	'gas': 2000000,
	'gasPrice':web3.toWei('50','gwei')
} 

# sign transaction 
signed_tx = web3.eth.account.signTransaction(tx,private_key)


# send transaction 

# get transaction hash 
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
